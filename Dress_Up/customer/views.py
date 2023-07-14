from typing import Any, Dict
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import View,TemplateView,ListView,DetailView
from store.models import Category,Outfit
from .models import Cart,Order
from django.contrib import messages
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

#auth_decorator

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please Login First!!")
            return redirect("log")
    return inner

dec=[signin_required,never_cache]

# Create your views here.

@method_decorator(dec,name="dispatch")
class CustomHomeView(TemplateView):
    template_name="cus-home.html"
    model=Category
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Category.objects.all()
        return context
    
@method_decorator(dec,name="dispatch")    
class DressCategoryView(TemplateView):
    template_name="dresscategory.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Category.objects.all()
        return context
@method_decorator(dec,name="dispatch")
class OutfitView(TemplateView):
    template_name="outfits.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Outfit.objects.all()
        return context
    
@method_decorator(dec,name="dispatch")        
class DressDetailsView(DetailView):
    template_name="dressdetails.html"
    model=Outfit
    context_object_name="outfit"
    pk_url_kwarg="did"
    
@method_decorator(dec,name="dispatch")    
class AddCart(View):
    def get(self,request,*args,**kwargs):
        drs=Outfit.objects.get(id=kwargs.get("id"))
        user=request.user
        Cart.objects.create(outfit=drs,user=user)
        messages.success(request,'Product added to cart!!')
        return redirect("home")

dec    
def deletecartitem(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,"Cart Item removed!!")
    return redirect("vcart")
    
@method_decorator(dec,name="dispatch")
class CartListView(ListView):
    template_name="cart-list.html"
    model=Cart  
    context_object_name="cartitem" 
    
    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user,status="cart")
        total=Cart.objects.filter(user=self.request.user,status="cart").aggregate(tot=Sum("outfit__price"))
        return ({'items':cart,"total":total})

@method_decorator(dec,name="dispatch")       
class CheckoutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get("cid")
        cart=Cart.objects.get(id=id)
        outf=cart.outfit
        user=request.user
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        Order.objects.create(outfit=outf,user=user,address=address,phone=phone)
        cart.status="Order Placed"
        cart.save()
        messages.success(request,"Order Placed Successfully!!")
        return redirect("home")

@method_decorator(dec,name="dispatch")  
class OrderListView(ListView):
    template_name="order-list.html"
    model=Order  
    context_object_name="orderitem"
    
    def get_queryset(self):
        order=Order.objects.filter(user=self.request.user)
        return ({"item":order})

dec
def deleteorderitem(request,id):
    order=Order.objects.get(id=id)
    order.status="Cancel Your Order"
    order.save()
    messages.error(request,"Order Cancelled!!")
    return redirect("vorder")

@method_decorator(dec,name="dispatch")
class OutfitinCatView(View):
   def get(self,request,*args,**kwargs):
     cid=kwargs.get("id")
     cat=Category.objects.get(id=cid)
     out=Outfit.objects.filter(category=cat)
     return  render(request,"catoutdet.html",{"out":out})
 
@method_decorator(dec,name="dispatch")
class SearchView(View):
    def get(self,request,*args,**kwargs):
        search=request.GET.get("search")
        outf=Outfit.objects.filter(name__icontains=search)
        context={"searchoutfit":outf}
        return render (request,'search.html',context)
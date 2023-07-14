from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from .forms import RegForm,LogForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LogView(FormView):
    template_name="log.html" 
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            user=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user_ob=authenticate(request,username=user,password=pswd)
            if user_ob:
                login(request,user_ob)
                messages.success(request,"Login Successful!!")
                return redirect("home")
        else:
            # messages.error(request,"Login Failed!! Invalid Username or password!")
            return render(request,"log.html",{"form":form_data})   
    
    
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")
    
class LgOut(View):
    def get(self,request):
        logout(request)
        return redirect("log")
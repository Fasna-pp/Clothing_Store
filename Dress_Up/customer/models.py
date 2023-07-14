from django.db import models
from store.models import Outfit
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    outfit=models.ForeignKey(Outfit,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")

class Order(models.Model):
    outfit=models.ForeignKey(Outfit,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    options=(
        ("Order Placed","Order Placed"),
        (" Order Packed"," Order Packed"),
        ("Shipped","Shipped"),
        ("Out For Delivery","Out For Delivery"),
        ("Order Delivered","Order Delivered"),
        ("Cancel Your Order","Cancel Your Order")
    )
    status=models.CharField(max_length=100,choices=options,default="Order Placed")
    date=models.DateField(auto_now_add=True)
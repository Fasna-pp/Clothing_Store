from django.db import models


# Create your models here.

    
class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to="category_image",null=True,blank=True)

    def _str_(self):
        return self.name
    
class Outfit(models.Model):
        name=models.CharField(max_length=100,null=False,blank=False)
        price=models.IntegerField()
        image=models.ImageField(upload_to="outfit_image",null=True,blank=True)
        description=models.CharField(max_length=500)
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        
         
        def _str_(self):
          return self.name
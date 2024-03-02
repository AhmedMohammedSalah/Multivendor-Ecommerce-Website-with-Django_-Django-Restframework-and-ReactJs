from django.db import models
from django.contrib.auth.models import User



# Vendor Models
class Vendor (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.user.username
# Product Category 
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    details=models.TextField(null=True)
    
    def __str__(self):
        return self.title
    
# Product  
class Product(models.Model):
    title = models.CharField(max_length=200)
    category =models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,blank=True, null=True)
    vendor =models.ForeignKey(Vendor, on_delete=models.SET_NULL,blank=True, null=True)
    details=models.TextField(null=True)
    price=models.FloatField()
    def __str__(self):
        return self.title 
    
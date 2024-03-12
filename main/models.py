from django.core.validators import MinValueValidator, MaxValueValidator
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
    category =models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,blank=True, null=True,related_name='category_product')
    vendor =models.ForeignKey(Vendor, on_delete=models.SET_NULL,blank=True, null=True)
    details=models.TextField(null=True)
    price=models.FloatField()
    def __str__(self):
        return self.title 
    
#Customer Model 
class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11)
    def __str__(self):
        return self.user.username
#Order Model
class Order (models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time=models.TimeField(  auto_now_add=True)
    def __unicode__(self):
        return '%s' % (self.order_time)

#Order Items Model  
class OrderItems (models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_items')   
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) :
        return self.product.title
    
    

#Address Model  
class Address (models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_address')   
    address =models.TextField()
    default_address=models.BooleanField()
    def __str__(self) :
        return self.address



#Product rating, review   
class ProductRating (models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_ratings')   
    product =models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_ratings')
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review =models.TextField()
    add_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"Rate: {self.rate}, Review: {self.review}"

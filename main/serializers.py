from rest_framework import serializers
from . import models

# Vendor
class VendorSerializers (serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        # fields='__all__'
        fields = ['id','user','address']
    
    def __init__(self, *args, **kwargs):
        super(VendorSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth=1
    
class VendorDetailSerializers (serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields = ['id','user','address']
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth=1

# products 
class ProductsSerializers (serializers.ModelSerializer):
    product_ratings=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title',
                  'details', 'price', 'product_ratings']

    def __init__(self, *args, **kwargs):
        super(ProductsSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ProductDetailSerializers (serializers.ModelSerializer):
    product_ratings=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title',
                    'details', 'price', 'product_ratings']

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
        
        
        
# Customer 

class CustomerSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        # fields='__all__'
        fields = ['id', 'user', 'mobile']

    def __init__(self, *args, **kwargs):
        super(CustomerSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CustomerDetailSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'mobile']

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

# Orders 


class OrderSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.Order
        # fields='__all__'
        fields = ['id', 'customer', 'order_time']

    def __init__(self, *args, **kwargs):
        super(OrderSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class OrderDetailSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        # fields='__all__'
        fields = ['id','order','product']
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

# Address


class AddressSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.Address
        # fields='__all__'
        fields = ['id', 'customer', 'address', 'default_address']

    def __init__(self, *args, **kwargs):
        super(AddressSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
# Product Rating and review
class ProductRatingSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields='__all__'
        # fields = ['id', 'customer', 'address', 'default_address']

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

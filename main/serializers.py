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
    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title', 'details', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductsSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ProductDetailSerializers (serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title', 'details', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializers, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
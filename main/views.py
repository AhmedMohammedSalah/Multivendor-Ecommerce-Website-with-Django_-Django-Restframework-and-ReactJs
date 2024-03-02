from django.shortcuts import render
from rest_framework import generics ,permissions
# Create your views here.
from . import models ,serializers
# vendors
class VendorList (generics.ListAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializers
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
class VendorDetail (generics.RetrieveAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializers
    # permission_classes=[permissions.IsAuthenticated]
# Products 


class ProductsList (generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductsSerializers
    
class ProductDetail (generics.RetrieveAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializers
from django.shortcuts import render
from rest_framework import generics, permissions,pagination,viewsets
# Create your views here.
from . import models, serializers
# vendors


class VendorList (generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializers
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class VendorDetail (generics.RetrieveAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializers
    # permission_classes=[permissions.IsAuthenticated]
# Products


class ProductsList (generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductsSerializers
    pagination_class=pagination.LimitOffsetPagination


class ProductDetail (generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializers


# Customer
class CustomerList (generics.ListAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.VendorSerializers


class CustomerDetail (generics.RetrieveAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.VendorDetailSerializers

#Order
class OrderList (generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializers

class OrderDetail (generics.RetrieveAPIView):
    # queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderDetailSerializers
    def get_queryset(self):
        order_id=self.kwargs['pk']
        order= models.Order.objects.get(id=order_id)
        order_items=models.OrderItems.objects.filter(order=order)
        return order_items
        
        
# Address

class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializers
    # def get_queryset(self):
    #     order_id=self.kwargs['pk']
    #     order= models.Order.objects.get(id=order_id)
    #     order_items=models.OrderItems.objects.filter(order=order)
    #     return order_items

# Product Rating and review
class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = models.ProductRating.objects.all()
    serializer_class = serializers.ProductRatingSerializers
    

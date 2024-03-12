from django.urls import path
from . import views
from rest_framework import routers

router =routers.DefaultRouter()
router.register('address',views.AddressViewSet)
router.register('reviews',views.ProductRatingViewSet)
name='main'
urlpatterns = [
    # Vendors
    path('vendors/',views.VendorList.as_view(),name='vendors'),
    path('vendors/<int:pk>',views.VendorDetail.as_view(),name='vendor_id'),
    # Products 
    path('products/', views.ProductsList.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_id'),
    # Customer
    path('customers/',views.CustomerList.as_view(),name='customers'),
    path('customer/<int:pk>',views.CustomerDetail.as_view(),name='customer_id'),
    # Order 
    path('orders/',views.OrderList.as_view(),name='orders'),
    path('order/<int:pk>',views.OrderDetail.as_view(),name='order_id'),
    
]

urlpatterns+=router.urls
from django.urls import path
from . import views
name='main'
urlpatterns = [
    path('vendors/',views.VendorList.as_view(),name='vendors'),
    path('vendors/<int:pk>',views.VendorDetail.as_view(),name='vendor_id'),
    # products 
    path('products/', views.ProductsList.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_id'),
    
    
]
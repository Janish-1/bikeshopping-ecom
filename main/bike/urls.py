from django.contrib import admin
from django.urls import path 
from . import views
from .views import *

urlpatterns = [
    path("" , views.home , name="home"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    # Make product_id optional with a default value of None
    path("products/<int:product_id>/", views.product_detail, name="product_detail"),

    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('contact/', contact_view, name='contact'),
    
    path('productmainpage/', views.productmainpage, name='productmainpage'),
    path('productadd/', views.productadd, name='productadd'),
    path('logout/', logout_view, name='logout')
    # path('contact_form/', contact_view, name='contact_view'),
]

from django.urls import path
from home.views import * 


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('',home,name='home'),
    path('products/<int:product_id>', product, name='product'),
    path('shop',shop,name='shop'),
    path('contact',contact,name='contact'),
    path('cart',cart,name='cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),  # Define the URL pattern for adding to cart
    path('login',login,name='login'),
    path('checkout',checkout,name='checkout'),
    path('register',register,name='register'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('logout/', logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
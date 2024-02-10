from django.utils.html import format_html
from django.contrib import admin
from .models import *

admin.site.register(Product)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'display_image')  # Replace 'image_tag' with the actual method name
#     search_fields = ('name', 'price')  # Add fields you want to be searchable in the admin interface

#     def display_image(self, obj):
#         return format_html('<img src="{}" width="50" height=50" />', obj.image.url)

#     display_image.short_description = 'Image'




@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message')
    search_fields = ('full_name', 'email', 'message')
# forms.py
from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']



from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'image_1', 'image_2', 'image_3', 'image_4']

    # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Product Image')
    # image_1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Product Image 1')
    # image_2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Product Image 2')
    # image_3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Product Image 3')
    # image_4 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Product Image 4')

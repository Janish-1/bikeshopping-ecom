
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import *

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password2)
            # login(request, user)

            # Add a success message
            # messages.success(request, '')

            # Redirect to a desired page, e.g., the home page
            return render(request,'bike/register.html'  ,{"message":"Registration successful. You are now logged in."})
        else:
            error_message = 'Passwords do not match.'
            # messages.error(request, error_message)
            return render(request, 'bike/register.html', {'error_message': error_message})

    return render(request, 'bike/register.html')



# views.py



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            return redirect('home')  
        else:
            return render(request, 'bike/login.html',{"message":"Invalid Username and Password"})

    return render(request, 'bike/login.html')

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
   
    return redirect('home')

from django.shortcuts import render
from .models import Product


def home(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    
    # Create a dictionary with the product data
    context = {'products': products}

    # Render the first HTML page with the product data
    return render(request, "bike/index.html", context)

def productmainpage(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    
    # Create a dictionary with the product data
    context = {'products': products}

    # Render the second HTML page with the product data
    return render(request, "bike/productmainpage.html", context)










def product_detail(request, product_id):
    # Retrieve the product details based on the product_id
    product = get_object_or_404(Product, pk=product_id)
    
    # Pass the product details to the template
    context = {'product': product}
    return render(request, 'bike/pppp.html', context)





def productadd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success') 
    else:
        form = ProductForm()

    return render(request, 'bike/productaddpage.html', {'form': form})





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! Thank you.')
            return redirect('contact') 
    else:
        form = ContactForm()

    return render(request, 'bike/contact.html', {'form': form})


from decimal import Decimal
@login_required(login_url='login')
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)

        quantity = 1 
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity <= 0:
                raise ValueError('Invalid quantity')
        except ValueError:
          
            return redirect('product_detail', product_id=product.id)

        
        price = float(product.price)
        total_cost = price * quantity

        cart = request.session.get('cart', [])
        cart_item = {
            'id': product.id,
            'image': product.image.url,
            'name': product.name,
            'price': price,  
            'quantity': quantity,
            'total_cost': total_cost,
        }
        cart.append(cart_item)
        request.session['cart'] = cart
        

       
        return redirect('cart')

    return redirect('home')

def cart(request):
    cart_items = request.session.get('cart', [])
    total_price = sum(item['total_cost'] for item in cart_items)
    return render(request, 'bike/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# views.py


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    for item in cart:
        if item['id'] == product_id:
            cart.remove(item)
            break 
    request.session['cart'] = cart
    return redirect('cart')  
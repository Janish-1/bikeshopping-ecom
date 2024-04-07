from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *

    
# def home(request):
#     prod = Product.objects.all()
#     cat=Category.objects.all()
#     context = {'prod': prod, 'cat': cat}
#     return render(request, 'index.html',context)


from random import shuffle

def home(request):
    prod = list(Product.objects.all())  # Convert queryset to list
    shuffle(prod)  # Shuffle the list randomly
    cat = Category.objects.all()
    context = {'prod': prod, 'cat': cat}
    return render(request, 'index.html', context)



def product(request, product_id):
    cat=Category.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product,'cat':cat}
    return render(request, 'product-single.html', context)


from django.shortcuts import render
from django.db.models import Q  # Import Q to use OR condition in filter
from .models import Category, Product

def shop(request):
    cat=Category.objects.all()
    categories = Category.objects.all()
    # Get the selected category name from the query parameters
    selected_category = request.GET.get('category')
    # Filter products based on the selected category if a category is selected
    if selected_category:
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()
    # Get the search query from the request parameters
    search_query = request.GET.get('search')
    # Filter products based on the search query if it exists
    if search_query:
        products = products.filter(Q(product_name__icontains=search_query))
    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'cat':cat
    }
    return render(request, 'shop.html', context)


from django.shortcuts import render, redirect


def contact(request):
    cat=Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message') 
        submission = ContactFormSubmission(name=name, email=email, subject=subject, message=message)
        submission.save()
        
        
        return redirect('contact')
    
    # Handle GET request or initial form load
    return render(request, 'contact.html',{'cat': cat})





def checkout(request):
    return render(request,'checkout.html')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    message = None
    if request.method == 'POST':
        name = request.POST.get('user')
        email = request.POST.get('emails')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            message = "Passwords do not match"
            return render(request, 'login.html', {'message': message})
        try:
            user = User.objects.create_user(email=email, password=password, username=name)
            user.save()
            message = "Registration successful. Please login."
            return render(request, 'login.html', {'message': message})
        except Exception as e:
            message = f"An error occurred: {e}"
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')




from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    cat=Category.objects.all()
    message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            authenticated_user = authenticate(request, username=user.username, password=password)
            print(user)
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                # Set success message
                message  = "Login successful."
                return redirect('login')  
            else:
                message = "Invalid email or password."
        except User.DoesNotExist:
            message = "Invalid email or password."
    return render(request, 'login.html', {'messages': message,'cat':cat})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def add_to_cart(request):
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        size_name = request.POST.get('size')
        quantity = request.POST.get('quantity', 1)
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError('Invalid quantity')
        except ValueError:
            pass
        product = get_object_or_404(Product, pk=product_id)
        size = product.sizes.filter(name=size_name).first()
        cart_item = {
            'product_id': product_id,
            'size_name': size_name,
            'quantity': quantity,
            'product_name': product.product_name,
            'product_price': product.product_price,
            'product_desc': product.product_desc,
            'product_image': product.product_image.url        
        }
        cart = request.session.get('cart', [])
        cart.append(cart_item)
        request.session['cart'] = cart
        return redirect('cart')
    else:
        return redirect('home')


# def cart(request):
#     cart = request.session.get('cart', [])  # Retrieve the cart from the session
#     context = {'cart': cart}
#     return render(request, 'cart.html', context)



from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def cart(request):
    cat=Category.objects.all()
    cart = request.session.get('cart', [])
    total_cost = 0
    for item in cart:
        item['total_cost'] = item['product_price'] * item['quantity']
        total_cost += item['total_cost']
    context = {'cart': cart, 'total_cost': total_cost,'cat':cat}
    return render(request, 'cart.html', context)


def remove_from_cart(request, product_id):
    if 'cart' in request.session:
        try:
            product_id = int(product_id)
            cart = request.session.get('cart', [])
            removed = False
            updated_cart = []
            for item in cart:
                if int(item.get('product_id')) == product_id and not removed:
                    removed = True
                else:
                    updated_cart.append(item)
            request.session['cart'] = updated_cart
        except ValueError:
            pass  # Handle invalid product ID
    return redirect('cart')



from django.contrib.auth import logout
def logout_view(request):
    logout(request)
   
    return redirect('home')

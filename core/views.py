from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem, Review, Wishlist, ShippingAddress
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, status='PENDING')
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.price = product.price * order_item.quantity
    order_item.save()
    return redirect('cart')

@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status='PENDING').first()
    return render(request, 'core/cart.html', {'order': order})

@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, status='PENDING').first()
    if request.method == 'POST':
        ShippingAddress.objects.create(
            user=request.user,
            order=order,
            address_line1=request.POST['address_line1'],
            city=request.POST['city'],
            state=request.POST['state'],
            postal_code=request.POST['postal_code'],
            country=request.POST['country'],
        )
        order.status = 'SHIPPED'
        order.save()
        return redirect('home')
    return render(request, 'core/checkout.html', {'order': order})

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(title__icontains=query) if query else []
    return render(request, 'core/search.html', {'results': results})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')  # Redirect to home after logout


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match.")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log in the user after registering
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'core/wishlist.html', {'wishlist_items': wishlist_items})



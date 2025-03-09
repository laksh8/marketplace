from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem, Review, Wishlist, ShippingAddress
from django.contrib.auth.models import User

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

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
    return render(request, 'cart.html', {'order': order})

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
    return render(request, 'checkout.html', {'order': order})

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(title__icontains=query) if query else []
    return render(request, 'search.html', {'results': results})

from django.shortcuts import render
from .models import Seller
from django.contrib.auth.models import User

def home(request):
    sellers = Seller.objects.all()
    return render(request, 'home.html', {'sellers': sellers})

def business(request):
    return render(request, 'business.html', {})

def about(request):
    return render(request, 'about.html', {})



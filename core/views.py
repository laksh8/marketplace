from django.shortcuts import redirect, render

from core.forms import SellerForm
from .models import Seller
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BuyerRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = BuyerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    sellers = Seller.objects.all()
    return render(request, 'home.html', {'sellers': sellers})

def business(request):
        if request.method == 'POST':
            form = SellerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/thank-you') 
        else:
            form = SellerForm()
        
        return render(request, 'business.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def about(request):
    return render(request, 'about.html', {})

def invest(request):
    return render(request, 'invest.html', {})

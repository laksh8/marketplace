from django.shortcuts import get_object_or_404, redirect, render

from core.forms import SellerForm
from core.utils.token_utils import generate_user_token
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

def gotoseller(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    token = generate_user_token(request.user)
    
    # Redirect to seller server with token in URL
    redirect_url = f"http://{seller.url}/?token={token}"
    return redirect(redirect_url)


def logout_view(request):
    logout(request)
    return redirect('/login')

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

# central_server/views.py

from django.http import JsonResponse
import os
import platform
from datetime import datetime

def health_check(request):
    try:
        # Example of checking if DB connection works
        from django.db import connection
        connection.ensure_connection()
        
        # Check server uptime or other system stats
        system_info = {
            "status": "ok",
            "timestamp": datetime.now().isoformat(),
            "server": platform.node(),
            "os": platform.system(),
            "version": platform.version(),
            "db_connected": connection.is_usable(),
            "uptime": os.popen("uptime -p").read().strip()  # You can customize the system info here
        }

        return JsonResponse(system_info)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


@login_required
def profile_view(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'profile.html', {'user': user})
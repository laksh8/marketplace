from django.shortcuts import redirect, render

from core.forms import SellerForm
from .models import Seller
from django.contrib.auth.models import User

def home(request):
    sellers = Seller.objects.all()
    return render(request, 'home.html', {'sellers': sellers})

def business(request):
        if request.method == 'POST':
            form = SellerForm(request.POST)
            if form.is_valid():
                # You can save to DB or send email here
                print(form.cleaned_data)  # replace with actual logic
                return redirect('/thank-you')  # Make a thank you page
        else:
            form = SellerForm()
        
        return render(request, 'business.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def about(request):
    return render(request, 'about.html', {})

def invest(request):
    return render(request, 'invest.html', {})



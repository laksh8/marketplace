from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from core.models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'email', 'description', 'logo']

class BuyerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
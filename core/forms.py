from django import forms

class SellerForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')
    description = forms.CharField(label='About Your Store', widget=forms.Textarea)
    logo = forms.ImageField(label='Store Logo')
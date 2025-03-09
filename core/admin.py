from django.contrib import admin

from core.models import Category, Order, Product, Profile

# Register your models here.

admin.site.register(Profile)
# admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
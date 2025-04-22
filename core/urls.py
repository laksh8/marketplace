from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.home, name='home'),
    path("business", views.business, name='business'),
    path("about", views.about, name = 'about'),
    path("invest", views.invest, name = 'invest'),
]

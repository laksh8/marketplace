from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"
urlpatterns = [
    path('', views.home, name='home'),
    path("business", views.business, name='business'),    
    path('thank-you', views.thank_you, name='thank_you'),
    path("about", views.about, name = 'about'),
    path("invest", views.invest, name = 'invest'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

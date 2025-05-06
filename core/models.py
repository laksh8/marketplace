from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Seller(models.Model):
    
    # details
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    under_verification = models.BooleanField(default=True)

    def __str__(self):
            return f"{self.name}"

class CustomUser(AbstractUser):
    # Force role to always be 'buyer'
    def save(self, *args, **kwargs):
        self.is_staff = False
        self.is_superuser = False
        super().save(*args, **kwargs)
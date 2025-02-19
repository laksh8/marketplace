from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

from django.db import models

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
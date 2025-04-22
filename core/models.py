from django.db import models

# Create your models here.

class Seller(models.Model):
    
    # details
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
            return f"{self.name}"
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Status(models.Model):
    name = models.CharField(max_length=20)
    sequence = models.FloatField()
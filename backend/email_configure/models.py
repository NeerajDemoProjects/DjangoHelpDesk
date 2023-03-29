from django.db import models
from django import forms
class Message(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()

class OutgoingEmailServer(models.Model):
    email_address = models.EmailField()
    email_password = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    port = models.IntegerField()




# Create your models here.

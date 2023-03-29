from django.contrib import admin
from .models import Ticket,Status
from email_configure.models import Message
admin.site.register(Ticket)
admin.site.register(Status)

admin.site.register(Message)

# Register your models here.

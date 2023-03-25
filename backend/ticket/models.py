from django.db import models
from contact.models import Contact,Status
# Create your models here.



class Ticket(models.Model):
    query = models.TextField()
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    state_id = models.ForeignKey(Status,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


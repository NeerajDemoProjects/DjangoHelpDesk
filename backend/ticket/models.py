from django.db import models
from contact.models import Contact,Status
# Create your models here.



class Ticket(models.Model):
    query = models.TextField(null = True)
    contact_id = models.ForeignKey(Contact,null = True, on_delete=models.CASCADE)
    state_id = models.ForeignKey(Status,null = True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


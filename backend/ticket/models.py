from django.db import models
from contact.models import Contact,Status
# Create your models here.

from django.db import models
from  email_configure.models import Message


CUSTOMER_RATE_CHOICES = (
    ("satisfied", "Satisfied"),
    ("unsatisfied", "Unsatisfied"),
)









class PrefixedSerialNumberField(models.CharField):
    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        kwargs.setdefault('max_length', 12)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['prefix'] = self.prefix
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        if add:
            last_number = model_instance.__class__.objects.order_by().last()
            if last_number:
                last_number = int(last_number.number[len(self.prefix):])
            else:
                last_number = 0
            number = last_number + 1
            model_instance.number = self.prefix + str(number).zfill(self.max_length - len(self.prefix))
        return super().pre_save(model_instance, add)



class Ticket(models.Model):
    number = PrefixedSerialNumberField(prefix='TKT/2022/', unique=True)
    query = models.TextField(null = True)
    contact_id = models.ForeignKey(Contact,null = True, on_delete=models.CASCADE)
    state_id = models.ForeignKey(Status,null = True,on_delete=models.CASCADE)
    message_ids = models.ManyToManyField(Message)
    created_at = models.DateTimeField(auto_now_add=True)
    is_expired = models.BooleanField(default=False)
    created_rating = models.DateTimeField()
    last_visited = models.DateTimeField()

    closed = models.BooleanField(default=False)
    is_rating = models.BooleanField(default=False)
    custom_rate = models.CharField(
        max_length=20,
        choices=CUSTOMER_RATE_CHOICES)
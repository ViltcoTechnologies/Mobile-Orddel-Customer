from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from client_app.models import *
from order.models import *
from delivery_app.models import *


class Invoice(models.Model):
    payment_by = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(OrderDetail, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True, blank=True)
    vat = models.FloatField(default=0.2)
    portrage_price = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    sales_price = models.FloatField(default=0.0)
    item = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)




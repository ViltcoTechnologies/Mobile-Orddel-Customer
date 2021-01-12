from django.db import models
from django.contrib.auth.models import User
from products.models import *

# Create your models here.

gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)


# Delivery Person registration model
class DeliveryPerson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    current_location = models.CharField(max_length=100)
    no_of_orders = models.IntegerField(default=0)
    buying_capacity = models.IntegerField(default=0, blank=True, null=True)
    total_amount_shopped = models.IntegerField(default=0, blank=True, null=True)
    gender = models.CharField(max_length=300, choices=gender_choices)
    image = models.ImageField(upload_to=f"delivery_person/photos/{user}/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.username)


# Vehicle registration model
class Vehicle(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    license_image_front = models.ImageField(upload_to=f"vehicle/photos/{id}/", null=True, blank=True)
    license_image_back = models.ImageField(upload_to=f"vehicle/photos/{id}/", null=True, blank=True)
    copy_image_front = models.ImageField(upload_to=f"vehicle/photos/{id}/", null=True, blank=True)
    copy_image_back = models.ImageField(upload_to=f"vehicle/photos/{id}/", null=True, blank=True)
    license_no = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class ConsolidatedPurchase(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    cost_per_unit = models.IntegerField()
    purchased_from = models.CharField(max_length=300)



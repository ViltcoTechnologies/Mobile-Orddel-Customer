from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Choices menu
gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')

    )

# business_choices = (
#     ('shop', 'Shop'),
#     ('restaurant', 'Restaurant'),
#     ('catering', 'Catering')
#
#
#     )
#
# business_type_choices = (
#     ('online', 'Online'),
#     ('physical', 'Physical')
#
#     )

# Many clients can be registered to a single package


class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Client registered


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    current_location = models.CharField(max_length=100)
    gender = models.CharField(max_length=300, choices=gender_choices)
    image = models.ImageField(upload_to=f"clients/photos/{user}/")
    number_of_order = models.IntegerField(default=0)
    total_amount_shopped = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


# Client can have multiple businesses
class BusinessDetail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    nature = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to=f"business/logo/{name}/", null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Client can have many shipment addresses
class ShipmentAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    shipment_address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)

# Client can have multiple bank accounts
class BankDetails(models.Model):
    client = models.ForeignKey(Client, on_delete = models.SET_NULL, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    branch_code = models.CharField(max_length=100, null=True, blank=True)
    credit_card_no = models.CharField(max_length=150, null=True, blank=True)
    sort_code = models.CharField(max_length=10, null=True, blank=True)
    credit_card_expiry = models.DateField(auto_now=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)



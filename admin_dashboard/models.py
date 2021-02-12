from django.db import models
from django.contrib.auth.models import User
from client_app.models import Client
from delivery_app.models import DeliveryPerson

# Create your models here.

gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

admin_approval_choices = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('unapproved', 'Unapproved'),
    ('cancelled', 'Cancelled')
)


class AdminUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=300, choices=gender_choices, null=True, blank=True)
    image = models.ImageField(upload_to=f"admin_user/photos/{User}", null=True, blank=True)
    admin_approval_status = models.CharField(max_length=300, choices=admin_approval_choices)
    date_created = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.username)


class ClientApprovalLog(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.ForeignKey(AdminUser, on_delete=models.SET_NULL, null=True, blank=True)
    admin_approval_status = models.CharField(max_length=300, choices=admin_approval_choices)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class DeliveryPersonApprovalLog(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.ForeignKey(AdminUser, on_delete=models.SET_NULL, null=True, blank=True)
    admin_approval_status = models.CharField(max_length=300, choices=admin_approval_choices)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)


class AdminUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=300, choices=gender_choices)
    image = models.ImageField(upload_to=f"delivery_person/photos/{user}", null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)


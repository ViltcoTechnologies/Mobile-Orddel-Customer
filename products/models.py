from django.db import models
from babel.numbers import list_currencies
from django.core.validators import MaxValueValidator, MinValueValidator


CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()]

unit_choices = (
    ('dozen', 'Dozen'),
    ('weight', 'Weight'),
    ('no', 'No')
)


class Category(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=50000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


# class SubCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=300, null=True, blank=True)
#
#     def __str__(self):
#         return str(self.name)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=50000, null=True, blank=True)
    short_description = models.CharField(max_length=800, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    unit = models.CharField(max_length=300, choices=unit_choices)
    avg_price = models.FloatField(default=0.0)
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.TextField()

    def __str__(self):
        return str(self.rating)

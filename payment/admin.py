from django.contrib import admin
from .models import *

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):


    list_display = ('id', 'payment_by', 'order', 'delivery_person', 'vat', 'portrage_price', 'profit',
                    'sales_price', 'item', 'date_created')
    list_display_links = ('payment_by', 'order', 'delivery_person')


admin.site.register(Invoice, InvoiceAdmin)
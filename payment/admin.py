from django.contrib import admin
from .models import *


class DeliveryNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'do_number')
    list_display_links = ('id', 'do_number')


admin.site.register(DeliveryNote, DeliveryNoteAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'inv_number', 'subtotal', 'portrage_price', 'profit', 'total', 'date_created')
    list_display_links = ('id', 'order', 'inv_number')


admin.site.register(Invoice, InvoiceAdmin)


class ItemUnitPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'unit_price', 'invoice')
    list_display_links = ('id', 'invoice')


admin.site.register(ItemUnitPrice, ItemUnitPriceAdmin)

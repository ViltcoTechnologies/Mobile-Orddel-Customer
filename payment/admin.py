from django.contrib import admin
from .models import *


class DeliveryNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'do_number')
    list_display_links = ('id', 'do_number')


admin.site.register(DeliveryNote, DeliveryNoteAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'inv_number', 'date_created')
    list_display_links = ('id', 'order', 'inv_number')


admin.site.register(Invoice, InvoiceAdmin)


class ItemUnitPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'unit_price', 'invoice')
    list_display_links = ('id', 'invoice')


admin.site.register(ItemUnitPrice, ItemUnitPriceAdmin)


class ClientPaymentDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'customer_id', 'payment_method_id')
    list_display_links = ('id', 'client')


admin.site.register(ClientPaymentDetails, ClientPaymentDetailAdmin)


class DeliveryPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'customer_id', 'payment_method_id')
    list_display_links = ('id', 'delivery_person')


admin.site.register(DeliveryPaymentDetails, DeliveryPaymentDetailsAdmin)
from django.contrib import admin
from .models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'client')
    list_display_links = ('client',)


admin.site.register(Cart, CartAdmin)


class CartProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'total_amount')
    list_display_links = ('cart',)


admin.site.register(CartProducts, CartProductsAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'purchase_order_no', 'order_title', 'delivery_person', 'order_created_datetime',
                    'order_delivery_datetime', 'shipment_address', 'delivery_notes', 'comment', 'distance', 'total_units_ordered',
                    'status', 'payment_type'

                    )
    list_display_links = ('cart', 'purchase_order_no', 'order_title')


admin.site.register(OrderDetail, OrderDetailAdmin)


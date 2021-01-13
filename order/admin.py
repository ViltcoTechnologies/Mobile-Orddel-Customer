from django.contrib import admin
from .models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'grand_total')
    list_display_links = ('client',)


admin.site.register(Cart, CartAdmin)


class AddToCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'total_amount')
    list_display_links = ('cart',)


admin.site.register(AddToCart, AddToCartAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_detail', 'purchase_order_no', 'order_title', 'delivery_person', 'order_created_datetime',
                    'order_delivery_datetime', 'shipment_address', 'delivery_notes', 'comment', 'distance', 'total_units_ordered',
                    'status', 'payment_type'

                    )
    list_display_links = ('order_detail', 'purchase_order_no', 'order_title')


admin.site.register(OrderDetail, OrderDetailAdmin)


class ConsolidatedPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'product', 'quantity', 'cost_per_unit', 'purchased_from')
    list_display_links = ('delivery_person', 'product')


admin.site.register(ConsolidatedPurchase, ConsolidatedPurchaseAdmin)

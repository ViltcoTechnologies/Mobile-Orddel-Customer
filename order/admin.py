from django.contrib import admin
from .models import *


class OrderBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'client')
    list_display_links = ('client',)


admin.site.register(OrderBox, OrderBoxAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_box', 'product', 'quantity', 'total_amount')
    list_display_links = ('order_box',)


admin.site.register(OrderProduct, OrderProductAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_box', '__str__', 'purchase_order_no', 'order_title', 'delivery_person', 'order_created_datetime',
                    'order_delivery_datetime', 'business', 'delivery_notes', 'comment', 'distance',
                    'status', 'payment_type'

                    )
    list_display_links = ('order_box', 'purchase_order_no', 'order_title')


admin.site.register(OrderDetail, OrderDetailAdmin)


from django.contrib import admin
from .models import *


class ConsolidatedPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_person', 'product', 'quantity', 'cost_per_unit', 'purchased_from')
    list_display_links = ('delivery_person', 'product')


admin.site.register(ConsolidatedPurchase, ConsolidatedPurchaseAdmin)

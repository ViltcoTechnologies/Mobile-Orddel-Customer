from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'company', 'is_available', 'unit', 'currency', 'category',
                    'date_created')
    list_display_links = ('category', 'sku', 'name')


admin.site.register(Product, ProductAdmin)


class AveragePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'avg_price', 'date_created')
    list_display_links = ('client', 'product', 'avg_price')


admin.site.register(AveragePrice, AveragePriceAdmin)



# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('id', 'client', 'product', 'rating', 'comment')
#     list_display_links = ('product',)


# admin.site.register(Review, ReviewAdmin)

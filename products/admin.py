from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'unit', 'avg_price', 'currency', 'category',
                    'date_created')
    list_display_links = ('category', 'sku', 'name')


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'rating', 'comment')
    list_display_links = ('product',)


admin.site.register(Review, ReviewAdmin)

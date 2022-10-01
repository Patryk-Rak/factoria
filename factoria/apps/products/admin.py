from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                          {'fields': ['product_name']}),
        ('Prize and stock information', {'fields': ['price', 'stock']}),
        ('category', {'fields': ['category'], 'classes': ['collapse']}),
    ]
    list_filter = ['price']
    search_fields = ['price']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

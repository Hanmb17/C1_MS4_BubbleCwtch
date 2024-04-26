from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Product Model Admin
    """
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'is_featured',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Model Admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

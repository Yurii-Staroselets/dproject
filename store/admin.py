from django.contrib import admin
from .models import Category1, Category2, Category3, Product


@admin.register(Category1)
class Category1Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category2)
class Category2Admin(admin.ModelAdmin):
    list_display = ['brand_name', 'slug']
    prepopulated_fields = {'slug': ('brand_name',)}


@admin.register(Category3)
class Category3Admin(admin.ModelAdmin):
    list_display = ['algorith_or_models', 'slug']
    prepopulated_fields = {'slug': ('algorith_or_models',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price',
                    'count', 'created', 'updated']
    list_filter = ['count', 'is_active']
    list_editable = ['price', 'count']
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.

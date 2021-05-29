from django.contrib import admin

"""
here detail and tell dejango to waht medels we want to access in admin area
"""
"""
here we impoert from our modesl 2 items to use admin
"""
from .models import Category, Product

"""
registering medels 
"""
@admin.register(Category)
class CatogoryAdmin(admin.ModelAdmin):
    """
    display item specific way
    """
    list_diplay = ['name', 'slug']
    """
    make slug populated automatically
    """
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price','in_stock','created','updated']
    """
    add some filter
    """
    list_filters = ['in_stock', 'is_active']
    """
    add some editable list
    """
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug': ('title',)}


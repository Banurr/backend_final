from django.contrib import admin
from .models import Category, Product, Comment


# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    search_fields = ('name', 'price')


admin.site.register(Category)
admin.site.register(Product, ShopAdmin)
admin.site.register(Comment)


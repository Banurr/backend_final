from django.contrib import admin
from .models import Category, Product, Comment


# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','category')
    search_fields = ('name', 'category')


admin.site.register(Category)
admin.site.register(Product, ShopAdmin)
admin.site.register(Comment)


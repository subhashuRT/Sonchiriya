from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('items','price', "stock","category","modified_date","is_available")
    prepopulated_field = {"slug":("items",)}

admin.site.register(Product,ProductAdmin)

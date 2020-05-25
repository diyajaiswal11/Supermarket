from django.contrib import admin

# Register your models here.
from .models import Product, Customer


admin.site.register(Product)
admin.site.register(Customer)
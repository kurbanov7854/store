from  django.contrib import  admin
from .models import *


class Product_top(admin.ModelAdmin):
    list_display = [ 'image', 'name', 'description','price']
admin.site.register(Product, Product_top)

admin.site.register([Order,AboutUs])


from django.contrib import admin
from .models import Order, Products
# Register your models here.
admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "E-Commerce Site"

class ProductAdmin(admin.ModelAdmin):
  list_display = ('title','price','category')
  search_fields = ('title','price','category')
  
class OrderAdmin(admin.ModelAdmin):
  list_display = ('name','total','email','state')
  search_fields = ('name','total','email','state')
  
admin.site.register(Products,ProductAdmin)
admin.site.register(Order,OrderAdmin)
from django.contrib import admin
from . models import Product,Order,OrededItem

# Register your models here.

class InsertAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','description','image')

admin.site.register(Product,InsertAdmin)
admin.site.register(Order)
admin.site.register(OrededItem)
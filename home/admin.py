from django.contrib import admin
from . models import Product,Order,OrededItem,Payment,Customer

# Register your models here.

class InsertAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','description','image')

admin.site.register(Product,InsertAdmin)

admin.site.register(Order)

class itemAdmin(admin.ModelAdmin):
    list_display = ('id','product','quantity','owner')

admin.site.register(OrededItem,itemAdmin)
admin.site.register(Payment)
admin.site.register(Customer)
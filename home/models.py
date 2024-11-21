from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone = models.CharField(max_length=10)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username


class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((ORDER_PROCESSED,'PROCESSED'),
                        (ORDER_DELIVERED,'DELIVERED'),
                        (ORDER_REJECTED,'REJECTED'),
                        (ORDER_CONFIRMED,'CONFIRMED'))
    order_status = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "order-{}-{}".format(self.id,self.owner)

class OrededItem(models.Model):
    product = models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

    def __str__(self):
        return str(self.product)

class Payment(models.Model):
    card_name = models.CharField(max_length=250)
    card_number = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
    cvv_number = models.CharField(max_length=100)

    def __str__(self):
        return self.card_name
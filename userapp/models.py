from django.db import models
from groceryapp.models import PRODUCTS
# Create your models here.


class CartItem(models.Model):
    product = models.ForeignKey(PRODUCTS, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"

    def save(self, *args, **kwargs):
        self.product_name = self.product.Productname
        self.price = self.product.Price
        self.total_price = self.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)
 
class Buynow(models.Model):
    product = models.ForeignKey(PRODUCTS, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"

    def save(self, *args, **kwargs):
        self.product_name = self.product.Productname
        self.price = self.product.Price
        self.total_price = self.price * self.quantity
        super(Buynow, self).save(*args, **kwargs)       


class BillingDetails(models.Model):
    cart = models.ForeignKey(CartItem, on_delete=models.CASCADE
                             )
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()



    def __str__(self):
        return self.name





class BuyBilling(models.Model):
    product = models.ForeignKey(PRODUCTS, on_delete=models.CASCADE
                             )
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()



    def __str__(self):
        return self.name





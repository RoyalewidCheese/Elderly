from django.db import models

# Create your models here.
class STORE(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100,null=True, blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)


class PRODUCTS(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)

class CATEGORY(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)
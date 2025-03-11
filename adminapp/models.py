from django.db import models

# Create your models here.

class ContactDb(models.Model):
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class UserRegistrationDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class HospitalRegistrationDb(models.Model):
    Hospitalname = models.CharField(max_length=100, null=True, blank=True, unique=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class DriverRegistrationDb(models.Model):
    Drivername = models.CharField(max_length=100, null=True, blank=True, unique=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class GroceryRegistration(models.Model):
    Groceryname = models.CharField(max_length=100, null=True, blank=True, unique=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
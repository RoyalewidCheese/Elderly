from django.db import models

# Create your models here.
class ProfileDB(models.Model):
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Timefrom = models.TimeField(null=True, blank=True)
    Timeto = models.TimeField(null=True, blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)

    def __str__(self):
        return self.FirstName

class Feedback(models.Model):
    driver = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.driver.FirstName}: {self.feedback}"

class TaxiBooking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    )

    FirstName = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    PickupLocation = models.CharField(max_length=100, null=True, blank=True)
    DestinationLocation = models.CharField(max_length=100, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)
    Driver = models.CharField(max_length=100, null=True, blank=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_amount = models.IntegerField(null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.FirstName}'s Booking"


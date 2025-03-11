

# Create your models here.
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    qualification = models.TextField()
    image = models.ImageField(upload_to='doctor_images/')


class Appointment(models.Model):
    date = models.DateField()
    time_slot = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.patient_name + " - " + str(self.date) + " " + self.time_slot

class Prescription(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    token_no = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    prescription = models.TextField()
    medicine = models.TextField(null=True)
    total_amount = models.IntegerField(null=True, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    status_choices = [('pending', 'Pending'), ('success', 'Success')]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return f"Prescription for {self.patient_name} - Token No: {self.token_no}"





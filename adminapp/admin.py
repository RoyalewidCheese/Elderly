from django.contrib import admin
from .models import *
from driverapp.models import *
from userapp.models import *
from groceryapp.models import *
from hosapp.models import *
# Register your models here.
#admin
admin.site.register(ContactDb)
admin.site.register(UserRegistrationDb)
admin.site.register(HospitalRegistrationDb)
admin.site.register(DriverRegistrationDb)
admin.site.register(GroceryRegistration)
#driver
admin.site.register(Feedback)
admin.site.register(ProfileDB)
admin.site.register(TaxiBooking)
#grocery
admin.site.register(STORE)
admin.site.register(PRODUCTS)
admin.site.register(CATEGORY)
#hospital
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Prescription)
#user
admin.site.register(CartItem)
admin.site.register(BillingDetails)

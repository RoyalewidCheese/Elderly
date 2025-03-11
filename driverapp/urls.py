from django.urls import path
from driverapp import views

urlpatterns = [
    path('driver_home/',views.driver_home,name="driver_home"),
    path('driver_logout/',views.driver_logout,name="driver_logout"),
    path('add_profile/',views.add_profile,name="add_profile"),
    path('profile_save/',views.profile_save,name="profile_save"),
    path('bookings/<vare>/',views.bookings,name="bookings"),
    path('generate_bill/<int:booking_id>/', views.generate_bill, name='generate_bill'),
    path('view_feedback/<varee>/', views.view_feedback, name='view_feedback'),
    path('view_pay/<vare>/', views.view_pay, name='view_pay'),




    # Add more URL patterns here as needed
]

from django.urls import path
from hosapp import views

urlpatterns = [
    path('hos_home/',views.hos_home,name="hos_home"),
    path('hosp_logout/',views.hosp_logout,name="hosp_logout"),
    path('doctor/',views.doctor,name="doctor"),
    path('doctor_save/',views.doctor_save,name="doctor_save"),
    path('doctor_display/',views.doctor_display,name="doctor_display"),
    path('dr_edit/<int:d_id>/', views.dr_edit, name="dr_edit"),
    path('dr_update/<int:d_id>/', views.dr_update, name="dr_update"),
    path('dr_delete/<int:d_id>/', views.dr_delete, name="dr_delete"),
#bookings
    path('appoinment_book/', views.appoinment_book, name="appoinment_book"),
    path('prescription/<int:p_id>/', views.prescription, name="prescription"),
    path('view_success_prescriptions/', views.view_success_prescriptions, name="view_success_prescriptions"),



]
from django.urls import path
from userapp import views
from userapp.views import *


urlpatterns = [
    path('',views.user_home,name="user_home"),
    path('user_sign_in_up/',views.user_sign_in_up,name="user_sign_in_up"),
    path('user_signup_save/',views.user_signup_save,name="user_signup_save"),
    path('user_sign_in/',views.user_sign_in,name="user_sign_in"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('user_about/',views.user_about,name="user_about"),
    path('user_contact/',views.user_contact,name="user_contact"),
    path('user_blog/',views.user_blog,name="user_blog"),
    path('contact_save/',views.contact_save,name="contact_save"),

#hosp
    path('hos_sign_in_up/',views.hos_sign_in_up,name="hos_sign_in_up"),
    path('hosp_signup_save/',views.hosp_signup_save,name="hosp_signup_save"),
    path('hosp_sign_in/',views.hosp_sign_in,name="hosp_sign_in"),


#grocery
    path('groc_sign_in_up/',views.groc_sign_in_up,name="groc_sign_in_up"),
    path('groc_signup_save/',views.groc_signup_save,name="groc_signup_save"),
    path('groc_sign_in/',views.groc_sign_in,name="groc_sign_in"),
    path('groc_pg/',views.groc_pg,name="groc_pg"),
    path('product_page/<path:cate>/', views.product_page, name="product_page"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    
    #  path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),
    
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('process-payment/', views.process_payment, name='process_payment'),
        path('process-payment-buy/<int:pk>/', views.process_payment_buy, name='buy_pay'),
    path('place/', views.place, name='place'),
        path('confirm/<int:pk>/', views.place1, name='confirm'),


#clinic
    path('clinicpg/', views.clinicpg, name='clinicpg'),
    path('clinicbook/', views.clinicbook, name='clinicbook'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('view_drbill/', views.view_drbill, name='view_drbill'),
    path('view_drpre/<int:b_id>/', views.view_drpre, name='view_drpre'),

    path('buy/<int:pk>/', views.checkout1, name='buy'),







#driver
    path('driver_sign_in_up/',views.driver_sign_in_up,name="driver_sign_in_up"),
    path('driver_sign_in/',views.driver_sign_in,name="driver_sign_in"),
    path('driver_signup_save/',views.driver_signup_save,name="driver_signup_save"),
    path('book_driver/',views.book_driver,name="book_driver"),
    path('driver_service/',views.driver_service,name="driver_service"),
    # path('driver_pro/',views.driver_pro,name="driver_pro"),
    path('taxibooking_save/',views.taxibooking_save,name="taxibooking_save"),
    path('view_status/',views.view_status,name="view_status"),
    path('view_bill/<int:booking_id>/', views.view_bill, name='view_bill'),
    path('create_order/<int:booking_id>/', views.create_order, name='create_order'),
    path('payment_complete/', views.payment_complete, name='payment_complete'),

    path('feedback_form/', views.feedback_form, name='feedback_form'),

    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),






]
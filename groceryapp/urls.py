from django.urls import path
from groceryapp import views

urlpatterns = [
    path('grocery_home/', views.grocery_home, name="grocery_home"),
    path('grocery_logout/',views.grocery_logout,name="grocery_logout"),
    path('store/',views.store,name="store"),
    path('store_save/',views.store_save,name="store_save"),
    path('add_category/',views.add_category,name="add_category"),
    path('category_save/',views.category_save,name="category_save"),
    path('add_products/',views.add_products,name="add_products"),
    path('product_save/',views.product_save,name="product_save"),
    path('orders/',views.orders,name="orders"),

]
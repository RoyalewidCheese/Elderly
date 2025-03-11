from django.shortcuts import render,redirect
import userapp.views
from groceryapp.models import STORE,PRODUCTS,CATEGORY
from userapp.models import BillingDetails
# Create your views here.
def grocery_home(request):

    return render(request, 'grocery_home.html', )
def grocery_logout(request):
    del request.session['Groceryname']
    del request.session['Password']
    return redirect(userapp.views.user_home)


def store(request):
    return render(request,'store.html')

def store_save(request):
    if request.method == "POST":
        n = request.POST.get('name')
        l = request.POST.get('mobile')
        e = request.POST.get('mail')
        s = request.POST.get('location')
        m = request.POST.get('dec')
        im = request.FILES['image']
        obj = STORE(Name=n,Mobile=l,Email=e,Location=s,Description=m,Image=im)
        obj.save()
        return redirect(grocery_home)

def add_products(request):
    cat = CATEGORY.objects.all()
    return render(request,'add_products.html',{'cat':cat})
def product_save(request):
    if request.method == "POST":
        n = request.POST.get('cate')
        l = request.POST.get('productname')
        e = request.POST.get('price')
        f = request.POST.get('quantity')
        im = request.FILES['image']
        obj = PRODUCTS(Category=n,Productname=l,Price=e,Quantity=f,Image=im)
        obj.save()
        return redirect(grocery_home)


def add_category(request):
    return render(request,'add_category.html')

def category_save(request):
    if request.method == "POST":
        n = request.POST.get('catname')
        l = request.POST.get('desc')
        im = request.FILES['image']
        obj = CATEGORY(CategoryName=n,Description=l,Image=im)
        obj.save()
        return redirect(grocery_home)


def orders(request):
    order = BillingDetails.objects.all()
    return render(request,'orders.html',{'order':order})
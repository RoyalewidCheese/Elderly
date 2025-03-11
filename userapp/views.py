from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from adminapp.models import ContactDb,UserRegistrationDb,HospitalRegistrationDb,DriverRegistrationDb,GroceryRegistration
from hosapp.views import hos_home
from driverapp.views import driver_home
from groceryapp.views import grocery_home
from driverapp.models import ProfileDB,TaxiBooking,Feedback
from groceryapp.models import *
from userapp.models import CartItem,BillingDetails,BuyBilling
from hosapp.models import Appointment, Doctor, Prescription
import razorpay
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

#user
def user_home(request):

    return render(request,'user_home.html')
def user_sign_in_up(request):
    return render(request,'user_signup_in.html')

def user_signup_save(request):
    if request.method == "POST":
        ab = request.POST.get('uname')
        bc = request.POST.get('mail')
        cd = request.POST.get('pass')
        obj = UserRegistrationDb(Username=ab,Email=bc,Password=cd)
        obj.save()
        return redirect(user_sign_in_up)

def user_sign_in(request):
    if request.method == "POST":
        ur = request.POST.get('uname')
        pd = request.POST.get('pass')
        if UserRegistrationDb.objects.filter(Username=ur,Password=pd).exists():

            request.session['Username'] = ur
            request.session['Password'] = pd

            return redirect(user_home)
        else:
            return redirect(user_signup_save)
    else:
        return redirect(user_signup_save)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(user_home)


def user_about(request):
    return render(request,'user_about.html')


def user_contact(request):
    store = CATEGORY.objects.all()
    return render(request,'user_contact.html', {'store': store})

def contact_save(request):
    if request.method == "POST":
        n = request.POST.get('first_name')

        e = request.POST.get('email')
        s = request.POST.get('subject')
        m = request.POST.get('message')
        obj = ContactDb(FirstName=n,Email=e,Subject=s,Message=m)
        obj.save()
        return redirect(user_contact)


def user_blog(request):
    return render(request,'user_blog.html')

#grocery
def groc_sign_in_up(request):
    return render(request,'grocery_signup_in.html')

def groc_signup_save(request):
    if request.method == "POST":
        ab = request.POST.get('storename')
        bc = request.POST.get('mail')
        cd = request.POST.get('pass')
        obj = GroceryRegistration(Groceryname=ab,Email=bc,Password=cd)
        obj.save()
        return redirect(groc_sign_in_up)

def groc_sign_in(request):
    if request.method == "POST":
        ur = request.POST.get('storename')
        pd = request.POST.get('pass')
        if GroceryRegistration.objects.filter(Groceryname=ur,Password=pd).exists():

            request.session['Groceryname'] = ur
            request.session['Password'] = pd

            return redirect(grocery_home)
        else:
            return redirect(groc_signup_save)
    else:
        return redirect(groc_signup_save)

#hospital

def hos_sign_in_up(request):
    return render(request,'hosp_signup_in.html')

def hosp_signup_save(request):
    if request.method == "POST":
        ab = request.POST.get('hosname')
        bc = request.POST.get('mail')
        cd = request.POST.get('pass')
        obj = HospitalRegistrationDb(Hospitalname=ab,Email=bc,Password=cd)
        obj.save()
        return redirect(hos_sign_in_up)

def hosp_sign_in(request):
    if request.method == "POST":
        ur = request.POST.get('hosname')
        pd = request.POST.get('pass')
        if HospitalRegistrationDb.objects.filter(Hospitalname=ur,Password=pd).exists():

            request.session['Hospitalname'] = ur
            request.session['Password'] = pd

            return redirect(hos_home)
        else:
            return redirect(hosp_signup_save)
    else:
        return redirect(hosp_signup_save)



def driver_sign_in_up(request):
    return render(request,'driver_signup_in.html')

def driver_signup_save(request):
    if request.method == "POST":
        ab = request.POST.get('drivername')
        bc = request.POST.get('mail')
        cd = request.POST.get('pass')
        obj = DriverRegistrationDb(Drivername=ab,Email=bc,Password=cd)
        obj.save()
        return redirect(driver_sign_in_up)

def driver_sign_in(request):
    if request.method == "POST":
        ur = request.POST.get('drivername')
        pd = request.POST.get('pass')
        if DriverRegistrationDb.objects.filter(Drivername=ur,Password=pd).exists():

            request.session['Drivername'] = ur
            request.session['Password'] = pd

            return redirect(driver_home)
        else:
            return redirect(driver_signup_save)
    else:
        return redirect(driver_signup_save)





def driver_service(request):
    driv = ProfileDB.objects.all()

    return render(request,'driver/driver_service.html',{'driv':driv})

def view_status(request):
    username = request.session.get('Username', None)
    if username:
        sta = TaxiBooking.objects.filter(FirstName=username)
    else:
        sta = TaxiBooking.objects.none()  # Return an empty queryset if user is not logged in

    return render(request, 'view_status.html', {'sta': sta})


# def view_bill(request, booking_id):
#     try:
#         booking = TaxiBooking.objects.get(id=booking_id)
#         total_amount = booking.total_amount
#
#         client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
#         payment = client.order.create({'amount': int(total_amount * 100), 'currency': "INR", 'payment_capture': '1'})
#
#         return render(request, 'bills.html', {'booking': booking, 'total_amount': total_amount, 'payment': payment})
#     except TaxiBooking.DoesNotExist:
#         return JsonResponse({'error': 'TaxiBooking not found'}, status=404)

def view_bill(request, booking_id):
    try:
        booking = TaxiBooking.objects.get(id=booking_id)
        total_amount = booking.total_amount

        client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
        payment = client.order.create({'amount': int(total_amount * 100), 'currency': "INR", 'payment_capture': '1'})

        # Check if payment ID is created
        if 'id' in payment:
            payment_id = payment['id']
            payment_status = 'success'
        else:
            payment_id = ''
            payment_status = 'pending'

        # Update the booking object with payment ID and status
        booking.payment_id = payment_id
        booking.payment_status = payment_status
        booking.save()

        return render(request, 'bills.html', {'booking': booking, 'total_amount': total_amount, 'payment': payment})
    except TaxiBooking.DoesNotExist:
        return JsonResponse({'error': 'TaxiBooking not found'}, status=404)




@csrf_exempt
def create_order(request,booking_id):
    if request.method == 'POST':
        client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
        booking = TaxiBooking.objects.get(id=booking_id)
        total = booking.total_amount
        amount = total * 100  # Amount in paise (e.g., ₹10 is 1000 paise)
        currency = 'INR'
        order = client.order.create({'amount': amount, 'currency': currency, 'payment_capture': '1'})
        return JsonResponse({'order_id': order['id'], 'amount': order['amount']})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def payment_complete(request):
    # This view can be used to handle the payment completion logic
    return render(request, 'payment_complete.html')


def book_driver(request):
    driver = ProfileDB.objects.all()
    return render(request,'driver/driver_book.html',{'driver':driver})
def taxibooking_save(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('mail')
        c = request.POST.get('mobile')
        d = request.POST.get('location1')
        e = request.POST.get('location2')
        f = request.POST.get('date')
        g = request.POST.get('time')
        h = request.POST.get('driver')
        obj = TaxiBooking(FirstName=a,Email=b,Mobile=c,PickupLocation=d,DestinationLocation=e,Date=f,Time=g,Driver=h)
        obj.save()
        return redirect(driver_service)

def feedback_form(request):
    driver_name = request.GET.get('driver_name')
    return render(request, 'driver/feedback_form.html', {'driver_name': driver_name})
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')
        driver_name = request.POST.get('driver_name')

        driver = ProfileDB.objects.get(FirstName=driver_name)  # Assuming FirstName is the field storing driver names
        feedback = Feedback(name=name, email=email, feedback=feedback_text, driver=driver)
        feedback.save()

        return redirect(user_home)


def groc_pg(request):
    store = CATEGORY.objects.all()

    # prod = PRODUCTS.objects.filter(Category=cate)

    return render(request,'grocery/grocerypg.html',{'store':store})

def product_page(request,cate):
    store = CATEGORY.objects.all()
    prod = PRODUCTS.objects.filter(Category=cate)
    return render(request,"grocery/products.html",{'prod':prod,'store':store})

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))

        product = PRODUCTS.objects.get(id=product_id)

        cart_item, created = CartItem.objects.get_or_create(product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
            cart_item.product_name = product.Productname

        cart_item.total_price = cart_item.price * cart_item.quantity
        cart_item.save()

        # Store the CartItem ID in the session
        request.session['cart_item_id'] = cart_item.id  # Assuming cart_item has a primary key named 'id'

    return redirect("cart_view")

# def add_to_cart(request):
#     if request.method == "POST":
#         product_id = request.POST.get("product_id")
#         quantity = int(request.POST.get("quantity", 1))
#
#         product = PRODUCTS.objects.get(id=product_id)
#
#         cart_item, created = CartItem.objects.get_or_create(product=product)
#
#         if not created:
#             cart_item.quantity += quantity
#         else:
#             cart_item.quantity = quantity
#             cart_item.product_name = product.Productname
#
#         cart_item.total_price = cart_item.price * cart_item.quantity
#         cart_item.save()
#
#     return redirect("cart_view")


# def buy_now(request, product_id, quantity=1):
#     try:
#         product = PRODUCTS.objects.get(id=product_id)

#         # Create or update the CartItem for the selected product and quantity
#         cart_item, created = CartItem.objects.get_or_create(product=product)

#         if not created:
#             cart_item.quantity += int(quantity)
#         else:
#             cart_item.quantity = int(quantity)
#             cart_item.product_name = product.Productname

#         cart_item.total_price = cart_item.price * cart_item.quantity
#         cart_item.save()

#         # Redirect to the checkout page after adding the item to the cart
#         return redirect('checkout')
#     except PRODUCTS.DoesNotExist:
#         # Handle the case where the product ID is invalid or not found
#         return redirect('grocery_pg')  # Redirect to the grocery page or any appropriate page


def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.total_price for item in cart_items)
    return render(request, "grocery/carts.html", {"cart_items": cart_items, "total_price": total_price})


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect("cart_view")

def checkout(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.total_price for item in cart_items)
    return render(request,'grocery/checkpout.html',{"cart_items": cart_items, "total_price": total_price})

def checkout1(request,**kwargs):
    # Retrieve all Buynow instances from the database
    id=kwargs.get('pk')
    item = PRODUCTS.objects.get(id=id)
    
    # Calculate the total price of all Buynow items
    total_price = item.Price
    
    return render(request, 'grocery/checkout.html', {"cart_items": item, "total_price": total_price})


def process_payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        state = request.POST.get('state')
        address = request.POST.get('addresss')
        town = request.POST.get('town')
        zip_code = request.POST.get('zip')
        phone = request.POST.get('phone')
        email = request.POST.get('mail')

        # Retrieve the CartItem ID from the session
        cart_item_id = request.session.get('cart_item_id')

        # Log the value of cart_item_id
        print("Cart Item ID:", cart_item_id)

        try:
            # Retrieve the CartItem instance
            cart_item = CartItem.objects.get(pk=cart_item_id)

            # Save the billing details with the CartItem ID to the database
            billing_details = BillingDetails(
                name=name,
                state=state,
                address=address,
                town=town,
                zip_code=zip_code,
                phone=phone,
                email=email,
                cart=cart_item  # Save the CartItem instance
            )
            billing_details.save()

            # Redirect to a success page or return a success message
            return redirect('place')
        except CartItem.DoesNotExist:
            # Handle the case where the CartItem does not exist
            print("CartItem does not exist.")

    return redirect('checkout')


def process_payment_buy(request,**kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')
        state = request.POST.get('state')
        address = request.POST.get('addresss')
        town = request.POST.get('town')
        zip_code = request.POST.get('zip')
        phone = request.POST.get('phone')
        email = request.POST.get('mail')

        # Retrieve the CartItem ID from the session
        buy = kwargs.get('pk')

        # Log the value of cart_item_id
        print("Cart Item ID:", buy)

        try:
            # Retrieve the CartItem instance
            cart_item = PRODUCTS.objects.get(pk=buy)

            # Save the billing details with the CartItem ID to the database
            billing_details = BuyBilling(
                name=name,
                state=state,
                address=address,
                town=town,
                zip_code=zip_code,
                phone=phone,
                email=email,
                product=cart_item  # Save the CartItem instance
            )
            billing_details.save()

            # Redirect to a success page or return a success message
            return redirect('confirm',pk=buy)
        except CartItem.DoesNotExist:
            # Handle the case where the CartItem does not exist
            print("CartItem does not exist.")

    return redirect('buy')




# def process_payment(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         state = request.POST.get('state')
#         address = request.POST.get('addresss')
#         town = request.POST.get('town')
#         zip_code = request.POST.get('zip')
#         phone = request.POST.get('phone')
#         email = request.POST.get('mail')
#
#         # Save the billing details to the database
#         billing_details = BillingDetails(
#             name=name,
#             state=state,
#             address=address,
#             town=town,
#             zip_code=zip_code,
#             phone=phone,
#             email=email,
#
#         )
#         billing_details.save()
#
#         # Redirect to a success page or return a success message
#         return redirect('place')
#
#     return redirect('checkout')  # Redirect back to the checkout page if the request method is not POST


# def place(request):
#     cart_items = CartItem.objects.all()
#     total_price = sum(item.total_price for item in cart_items)
#     return render(request,'grocery/place.html',{"cart_items": cart_items, "total_price": total_price})

def place(request):
    if request.method == 'POST':
        total_amount = request.POST.get('total_amount')  # Assuming total_amount is posted from the form
        client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
        payment = client.order.create({'amount': int(total_amount) * 100, 'currency': "INR", 'payment_capture': '1'})

        return render(request, 'payment_form.html', {'payment': payment})

    cart_items = CartItem.objects.all()
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'grocery/place.html', {"cart_items": cart_items, "total_price": total_price})



def place1(request,**kwargs):
    if request.method == 'POST':
        total_amount = request.POST.get('total_amount')  # Assuming total_amount is posted from the form
        client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
        payment = client.order.create({'amount': int(total_amount) * 100, 'currency': "INR", 'payment_capture': '1'})

        return render(request, 'payment_form.html', {'payment': payment})
    id = kwargs.get('pk')
    cart_items = PRODUCTS.objects.get(id=id)
    total_price = cart_items.Price
    return render(request, 'grocery/place1.html', {"item": cart_items, "total_price": total_price})









#clinic
def clinicbook(request):
    return render(request,'clinic/clinicbook.html')


def clinicpg(request):
    dr = Doctor.objects.all()
    return render(request,'clinic/clinicpg.html',{'dr':dr})


def book_appointment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time_slot = request.POST.get('time')
        user_name = request.POST.get('user')
        patient_name = request.POST.get('patient')
        patient_age = request.POST.get('age')
        patient_gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        appointment = Appointment(date=date, time_slot=time_slot, user_name=user_name, patient_name=patient_name,
                                   patient_age=patient_age, patient_gender=patient_gender, phone=phone)
        appointment.save()

    return redirect('clinicpg')




def view_drbill(request):

    username = request.session.get('Username', None)
    if username:
        pre = Prescription.objects.filter(user_name=username)
    else:
        pre = Prescription.objects.none()  # Return an empty queryset if user is not logged in

    return render(request,'clinic/clinic_bill.html',{'pre':pre})



def view_drpre(request, b_id):
    try:
        booking = Prescription.objects.get(id=b_id)
        total_amount = booking.total_amount
        client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
        payment = client.order.create({'amount': int(total_amount * 100), 'currency': "INR", 'payment_capture': '1'})

        # Check if payment ID is created
        if 'id' in payment:
            payment_id = payment['id']
            status = 'success'
        else:
            payment_id = ''
            status = 'pending'

        # Update the Prescription object with payment ID and status
        booking.payment_id = payment_id
        booking.status = status
        booking.save()

        return render(request, 'clinic/clinic_pre.html', {'booking': booking, 'total_amount': total_amount, 'payment': payment})
    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found'}, status=404)




# def view_drpre(request,b_id):
#     try:
#         booking = Prescription.objects.get(id=b_id)
#         total_amount = booking.total_amount
#         client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
#         payment = client.order.create({'amount': int(total_amount * 100), 'currency': "INR", 'payment_capture': '1'})
#         return render(request, 'clinic/clinic_pre.html', {'booking': booking, 'total_amount': total_amount, 'payment': payment})
#     except Prescription.DoesNotExist:
#         return JsonResponse({'error': 'TaxiBooking not found'}, status=404)


# def view_drpre(request, b_id):
#     try:
#         booking = Prescription.objects.get(id=b_id)
#         total_amount = booking.total_amount
#         client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
#         payment = client.order.create({'amount': int(total_amount * 100), 'currency': "INR", 'payment_capture': '1'})
#
#         # Assuming payment is successful
#         payment_id = payment['id']  # Retrieve payment ID from Razorpay response
#
#         # Create a Payment object
#         Payment.objects.create(booking=booking, payment_id=payment_id, status='success')
#
#         return render(request, 'clinic/clinic_pre.html', {'booking': booking, 'total_amount': total_amount, 'payment': payment})
#     except Prescription.DoesNotExist:
#         return JsonResponse({'error': 'Prescription not found'}, status=404)



# def view_bill(request, booking_id):
#     try:
#         booking = TaxiBooking.objects.get(id=booking_id)
#         total_amount = booking.total_amount
#
#         client = razorpay.Client(auth=('rzp_test_Yth6NFWjeeRvSw', 'eNEhfjXVCd9Wby7lZ48MaKbU'))
#         payment = client.order.create({'amount': int(total_amount * 100), 'currency': "INR", 'payment_capture': '1'})
#
#         return render(request, 'bills.html', {'booking': booking, 'total_amount': total_amount, 'payment': payment})
#     except TaxiBooking.DoesNotExist:
#         return JsonResponse({'error': 'TaxiBooking not found'}, status=404)


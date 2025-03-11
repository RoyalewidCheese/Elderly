from django.shortcuts import render,redirect
import userapp.views
from driverapp.models import ProfileDB,TaxiBooking,Feedback
from django.contrib.auth.decorators import login_required

# Create your views here.
def driver_home(request):
    wat = ProfileDB.objects.all()
    return render(request, 'driver_home.html', {'wat': wat})


def bookings(request, vare):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        status = request.POST.get('status')
        if status == 'accepted':
            TaxiBooking.objects.filter(id=booking_id).update(Status='Accepted')
        elif status == 'rejected':
            TaxiBooking.objects.filter(id=booking_id).update(Status='Rejected')
        return redirect('bookings', vare=vare)

    book = TaxiBooking.objects.filter(Driver=vare)
    return render(request, 'bookings.html', {'book': book})



def driver_logout(request):
    del request.session['Drivername']
    del request.session['Password']
    return redirect(userapp.views.user_home)


def add_profile(request):
    return render(request,'add_profile.html')

def profile_save(request):
    if request.method == "POST":
        n = request.POST.get('firstname')

        l = request.POST.get('mobile')
        e = request.POST.get('mail')
        s = request.POST.get('location')
        m = request.POST.get('fromtime')
        i = request.POST.get('timeto')
        im = request.FILES['image']
        obj = ProfileDB(FirstName=n,Mobile=l,Email=e,Location=s,Timefrom=m,Timeto=i,Image=im)
        obj.save()
        return redirect(driver_home)



def generate_bill(request, booking_id):
    # Retrieve the booking object
    booking = TaxiBooking.objects.get(id=booking_id)

    if request.method == 'POST':
        # Update the booking with the entered total amount and save it
        total_amount = request.POST.get('amount')
        booking.total_amount = total_amount
        booking.save()
        return redirect('driver_home')

    # Render the bill template with the updated booking details
    return render(request, 'billtemplate.html', {'booking': booking})



def view_feedback(request, varee):


    feedbacks = Feedback.objects.filter(driver=varee)
    return render(request, 'view_feedback.html', {'feedbacks': feedbacks})


def view_pay(request, vare):
    # Query for bookings with status = 'Accepted'
    accepted_bookings = TaxiBooking.objects.filter(Driver=vare, Status='Accepted')

    # Pass the accepted_bookings to the template for rendering
    return render(request, 'paysta.html', {'accepted_bookings': accepted_bookings})

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

import userapp.views
from hosapp.models import Doctor,Appointment,Prescription
# Create your views here.
def hos_home( request):

    return render(request,'hos_home.html')

def hosp_logout(request):
    del request.session['Hospitalname']
    del request.session['Password']
    return redirect(userapp.views.user_home)


def doctor(request):
    return render(request,'doctor.html')

def doctor_save(request):
    if request.method == "POST":
        n = request.POST.get('doctorname')
        l = request.POST.get('department')
        e = request.POST.get('qualification')
        im = request.FILES['image']
        obj = Doctor(name=n,department=l,qualification=e,image=im)
        obj.save()
        return redirect(hos_home)


def doctor_display(request):
    dr = Doctor.objects.all()
    return render(request,'display_dr.html',{'dr':dr})


def dr_edit(request,d_id):
    drt = Doctor.objects.get(id=d_id)
    return render(request, "edit_dr.html", {'drt': drt})

def dr_update(request,d_id):
    if request.method=="POST":
        a = request.POST.get('doctorname')
        b = request.POST.get('department')
        d = request.POST.get('qualification')
        try:
            c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(c.name, c)
        except MultiValueDictKeyError:
            file = Doctor.objects.get(id=d_id).name
        Doctor.objects.filter(id=d_id).update(name=a,department=b,qualification=d,image=file)
        return redirect(doctor_display)

def dr_delete(request, d_id):
    delcat = Doctor.objects.filter(id=d_id)
    delcat.delete()
    return redirect(doctor_display)


def appoinment_book(request):
    slots = Appointment.objects.all()
    return render(request,'display_booking.html',{'slots':slots})


def prescription(request, p_id):
    pre = Appointment.objects.get(id=p_id)

    if request.method == 'POST':
        token_no = pre.id  # Assuming token_no is the same as the appointment id
        patient_name = pre.patient_name
        date = pre.date
        age = pre.patient_age
        gender = pre.patient_gender
        user_name = pre.user_name
        medicine = request.POST.get('medicine')
        prescription = request.POST.get('presc')
        total_amount = request.POST.get('amount')

        # Create a new Prescription object and save it to the database
        prescription_obj = Prescription.objects.create(
            token_no=token_no,
            patient_name=patient_name,
            date=date,
            age=age,
            gender=gender,
            user_name = user_name,
            medicine=medicine,
            prescription=prescription,
            total_amount=total_amount
        )
        prescription_obj.save()

        # Redirect to a success page or render a template
        return redirect('hos_home')

    return render(request, 'prescription.html', {'pre': pre})
# Assuming you have a view function to handle this request
def view_success_prescriptions(request):
    # Query for prescriptions with status = 'success'
    success_prescriptions = Prescription.objects.all()

    # Pass the success_prescriptions to the template for rendering
    return render(request, 'view_paid.html', {'success_prescriptions': success_prescriptions})

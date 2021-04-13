from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import Http404

# Create your views here.


def home(request):
    profile=Person.objects.filter(doctor=True).order_by("-id")[0:4]
    context={"profiles":profile}
    return render(request,"home.html",context)

def person(request,id):
    profile=get_object_or_404(Person,id=id)
    clinic=Clinic.objects.filter(doctor_id=profile.id).order_by("-id")
    reserve=Reservation.objects.filter(doctor_id=profile.id)
    context={"profiles":profile,"clinics":clinic,"reservations":reserve}
    return render(request,"profile.html",context)
@login_required()
def add_clinic(request,id):
    doctor=get_object_or_404(Person,id=id)
    if doctor.doctor ==True:
        form=ClinicForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.doctor = request.user
            instance.save()
            messages.success(request,"your  clinic has been added")
            return redirect(reverse("home:profile",kwargs={"id":id}))
    else:
        raise Http404
    context={"form":form}
    return render(request,"add-clinic.html",context)

@login_required()
def add_reservation(request,id):
    person_clinic=Clinic.objects.get(id=id)
    new_clinic=get_object_or_404(Clinic,id=person_clinic.id)
    person=Person.objects.get(name=person_clinic.doctor)
    form=ReserveForm()
    form=ReserveForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.clinic = new_clinic
        instance.patient = request.user
        new_clinic.reservations +=1
        new_clinic.save()
        instance.save()
        messages.success(request,"your reservation has been added")
        return redirect(reverse("home:profile",kwargs={"id":person.id}))

    context={"form":form}
    return render(request,"reserve.html",context)


def appointment(request,id):
    if not request.user.is_authenticated:
        messages.success(request,"sign in first ")
        return redirect(reverse("account_login"))
    profile=Person.objects.get(id=id)
    reserve=Reservation.objects.filter(patient=request.user).order_by("-id")
    context={"profiles":profile,"reservation":reserve}
    return render(request,"appointment.html",context)


def delete(request,id):
    reserve=get_object_or_404(Reservation,id=id)
    person =Person.objects.get(id=reserve.patient.id)
    if request.user != reserve.patient or person.doctor == True:
        raise Http404
    else:        
        reserve.delete()
        messages.success(request,"your reservation has been deleted")
        return redirect(reverse("home:appointment",kwargs={"id":reserve.patient.id}))

def doctor(request):
    profile=Person.objects.filter(doctor=True).order_by("-id")
   
    context={"profiles":profile}
    return render(request,"doctors.html",context)

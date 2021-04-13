from django.urls import path
from . import views
from .views import *


app_name="doctor"

urlpatterns = [
    path('',views.home,name="doctor-home"),
    path('profile/<id>/',views.person,name="profile"),
    path('clinic/<id>/',views.add_clinic,name="clinic"),
    path('reserve/<id>/',views.add_reservation,name="reserve"),
    path('appointments/<id>/',views.appointment,name="appointment"),
    path('delete/<id>/',views.delete,name="delete"),
    path('doctors/',views.doctor,name="doctor"),

]

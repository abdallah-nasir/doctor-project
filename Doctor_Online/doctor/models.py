from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.



class Clinic(models.Model):
    doctor=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField(default=0)
    date=models.DateField(auto_now_add=True)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(auto_now_add=True)
    reservations=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Person(models.Model):
    name= models.OneToOneField(User,max_length=50,default=1,on_delete=models.CASCADE)
    image=models.ImageField(default="user-icon.png")
    doctor=models.BooleanField(default=False)
    patient=models.BooleanField(default=False)
   

    
    def get_absolute_url(self):
        return reverse('home:profile',kwargs={'id':self.id})

    class Meta:
        ordering=["-id"]
    def __str__(self):
        return self.name.username

    @receiver(post_save, sender=User)
    def create_user_Person(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(name=instance)


class Reservation(models.Model):
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    patient = models.ForeignKey(User,related_name="patient",on_delete=models.CASCADE)
    doctor = models.ForeignKey(User,related_name="doctor",on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time= models.TimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    def get_reserve_url(self):
        return reverse('home:reserve',kwargs={'id':self.id})

    def __str__(self):
        return self.name


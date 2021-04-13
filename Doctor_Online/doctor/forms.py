from django import forms 
from .models import Person,Clinic,Reservation
from allauth.account.forms import SignupForm
from bootstrap_datepicker_plus import DatePickerInput,TimePickerInput,DateTimePickerInput
TYPE=(
    ("patient","patient"),
    ("doctor","doctor")
)

class MyCustomSignupForm(SignupForm):
    account_type = forms.ChoiceField(choices=TYPE)
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        data =self.cleaned_data["account_type"]
        if data =="patient":
            person=Person.objects.get(id=user.id)
            person.patient=True
            person.save()
        if data =="doctor":
            person=Person.objects.get(id=user.id)
            person.doctor=True
            person.save()
        # Add your own processing here.
        user.save()
        # You must return the original result.
        return user


class ClinicForm(forms.ModelForm):
    date =forms.DateField(widget=DatePickerInput())
    start_time =forms.TimeField(widget=TimePickerInput())
    end_time=forms.TimeField(widget=TimePickerInput())
    class Meta:
        model = Clinic
        fields="__all__"
        exclude=["doctor"]


class ReserveForm(forms.ModelForm):
    date =forms.DateField(widget=DatePickerInput())
    time =forms.TimeField(widget=TimePickerInput())
    class Meta:
        model = Reservation
        fields= "__all__"
        exclude=["patient","clinic"]

   
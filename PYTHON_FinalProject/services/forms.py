from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'first_name', 'last_name', 'phone_number', 'recurrence']


class AppointmentDetailsForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

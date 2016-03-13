# -*- coding: utf-8 -*- 
from django import forms
from appointments.models import Appointment



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

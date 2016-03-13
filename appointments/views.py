# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.mail import mail_admins
from appointments.forms import AppointmentForm
from appointments.models import Appointment

class AppointmentView(CreateView):
    model = Appointment
    template_name = 'appointment.html'
    form_class = AppointmentForm
    context_object_name = 'form'
    success_url = reverse_lazy('appointment')
    
    def get_context_data(self, **kwargs):
        context = super(AppointmentView, self).get_context_data(**kwargs)
        context['title'] = "Запись на ремонт"
        return context 

    def form_valid(self, form):
        appointment = form.save()
        messages.success(self.request, u"Спасибо за Ваше сообщение! Наш менеджер перезвонит Вам!")
        mail_admins(appointment.name, appointment.phone, appointment.message)
        return super(AppointmentView, self).form_valid(form)

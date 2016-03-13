from django.contrib import admin
from appointments.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'brand_auto', 'create_date')

admin.site.register(Appointment, AppointmentAdmin)

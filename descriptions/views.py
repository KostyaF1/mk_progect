from django.views.generic.list import ListView
from descriptions.models import AppointmentOnline

class AppListView(ListView):
    model = AppointmentOnline
       
    def get_queryset(self):
        online = AppointmentOnline.objects.all()
        return online

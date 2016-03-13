from django.views.generic import TemplateView
from services.models import Service
from descriptions.models import AppointmentOnline

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['online'] = AppointmentOnline.objects.all()
        return context




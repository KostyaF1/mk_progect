# -*- coding: utf-8 -*- 
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy, reverse
from services.models import Service

class ServiceListView(ListView):
    model = Service
    
    def get_queryset(self):
        services = Service.objects.all()
        return services

# -*- coding: utf-8 -*- 
from django.views.generic.list import ListView
from slides.models import Slide

class SlideListView(ListView):
    model = Slide
       
    def get_queryset(self):
        slides = Slide.objects.all()
        return slides

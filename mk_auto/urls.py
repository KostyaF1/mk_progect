from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from mk_auto import views
from feedbacks.views import FeedbackView
from appointments.views import AppointmentView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mk_auto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^appointment/$', AppointmentView.as_view(), name='appointment'), 
    #url(r'^$', SlideListView.as_view(), name="index"),
    url(r'^slides/', include('slides.urls', namespace="slides")),   
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

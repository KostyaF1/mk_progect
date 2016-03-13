from django.conf.urls import patterns, include, url
from services import views

urlpatterns = patterns('',
    url(r'^$', views.ServiceListView.as_view(), name='list_view'),
)

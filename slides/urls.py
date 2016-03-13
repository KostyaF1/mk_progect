from django.conf.urls import patterns, include, url
from slides import views

urlpatterns = patterns('',
    url(r'^$', views.SlideListView.as_view(), name='list_view'),
)


from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^foodtrucks/$', include('foodtrucks.urls',namespace='foodtrucks')),
)

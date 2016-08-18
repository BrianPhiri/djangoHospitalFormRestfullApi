from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns(
    'api.views',
    url(r'^hosptital/', 'patient_list', name="hosptial"),
    url(r'^hospital/patient/(?P<pk>[0-9]+)$>', 'patient_detail', name="patient"),
)

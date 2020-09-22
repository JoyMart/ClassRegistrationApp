from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin_console', views.admin_console, name='admin_console'),
]



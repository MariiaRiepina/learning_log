"""Defines URL patterns for users"""
from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'locations'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('locations.urls')),
    path('locations/add/', views.add_location, name='add_location'),
]


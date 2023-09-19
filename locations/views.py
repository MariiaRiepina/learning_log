from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from learning_logs.models import Locations
from learning_logs.forms import TopicForm, EntryForm, LocationForm

class LocationsListView(ListView):
    model = Locations
    template_name = 'locations/location_list.html'
    context_object_name = 'locations'

class LocationsDetailView(DetailView):
    model = Locations
    template_name = 'locations/location_detail.html'
    context_object_name = 'location'

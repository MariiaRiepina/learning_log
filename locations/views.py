from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, Locations
from .forms import TopicForm, EntryForm, LocationForm

@login_required
def new_location(request, location_id):
    location = Locations.objects.get(id=location_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.location = location
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:location', args=[location_id]))

    context = {'location': location, 'form': form}
    return render(request, 'learning_logs/location_list.html', context)

# Create your views here.

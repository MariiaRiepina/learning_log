from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.db import IntegrityError

from django.contrib.auth.models import User
from learning_logs.models import UserProfile
from learning_logs.forms import CustomUserCreationForm

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Create a User object (not UserProfile) and set its username and password
                user = form.save(commit=False)
                user.username = form.cleaned_data['username']
                user.set_password(form.cleaned_data['password1'])
                user.save()

                # Get the selected location from the form
                selected_location = form.cleaned_data['location']

                # Create a UserProfile object linked to the User
                user_profile = UserProfile(user=user, location=selected_location)
                user_profile.save()

                login(request, user)
                return redirect('learning_logs:index')
            except IntegrityError:
                form.add_error('username', 'This username is already taken. Please choose a different one.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


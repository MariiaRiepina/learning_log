from django import forms
from .models import Topic, Entry, Locations ,UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    location = forms.ModelChoiceField(queryset=Locations.objects.all(),
                                              label='Location',
                                              required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.location = self.cleaned_data['location']
        if commit:
            user.save()
        return user

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


HIERARCHY_CHOICES = (
    (1, '1st lvl'),
    (2, '2nd lvl'),
    (3, '3rd lvl'),
    (4, '4th lvl'),
)
class LocationForm(forms.ModelForm):
    hierarchy_level = forms.IntegerField(label='Hierarchy Level',
                                         widget=forms.Select(choices=HIERARCHY_CHOICES),
                                         required=True)

    parent_location = forms.ModelChoiceField(queryset=Locations.objects.all(),
                                             label='Parent Location',
                                             required=False)
    class Meta:
        model = Locations
        fields = ['name', 'description', 'hierarchy_level', 'parent_location']


# Deleting unnecessary field username in extra panel
class UserProfileAdminForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['username']

class ChangeLocationForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        queryset=UserProfile.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Users'
    )
    new_location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        label='New Location'
    )
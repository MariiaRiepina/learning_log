from django import forms
from .models import Topic, Entry, Locations
from django.contrib.auth.models import User


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
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                           label='Users',
                                           widget=forms.CheckboxSelectMultiple,
                                           required=False)

    hierarchy_level = forms.IntegerField(label='Hierarchy Level',
                                         widget=forms.Select(choices=HIERARCHY_CHOICES),
                                         required=True)

    parent_location = forms.ModelChoiceField(queryset=Locations.objects.all(),
                                             label='Parent Location',
                                             required=False)

    class Meta:
        model = Locations
        fields = ['name', 'description', 'hierarchy_level', 'parent_location', 'users']


class AssignUserToLocationForm(forms.Form):
    location = forms.ModelChoiceField(queryset=Locations.objects.all(), label='Location')
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label='Users',
                                           widget=forms.CheckboxSelectMultiple)

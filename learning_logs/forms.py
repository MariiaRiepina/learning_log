from django import forms
from .models import Topic, Entry, Locations

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

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ['name', 'description', 'parent_location', 'hierarchy_level']

    hierarchy_level = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_location'].queryset = Locations.objects.filter(hierarchy_level=self.instance.hierarchy_level - 1)

    def clean(self):
        cleaned_data = super().clean()
        parent_location = cleaned_data.get("parent_location")

        if not parent_location:
            raise forms.ValidationError("Please select a parent_location")

        return cleaned_data





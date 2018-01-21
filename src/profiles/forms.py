from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dob', 'divorced', 'divorced_number', 'children', 'children_number', 'description']

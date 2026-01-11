from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'year',
            'majors_minors',
            'gender',
            'preferred_meeting_times',
            'preferred_meeting_location',
        ]

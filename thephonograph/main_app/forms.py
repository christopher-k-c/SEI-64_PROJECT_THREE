from django.forms import ModelForm
from .models import Tracklist
from django import forms
# test

class TracklistForm(forms.ModelForm):

    class Meta:
        model = Tracklist
        fields = ['track_name', 'track_duration']






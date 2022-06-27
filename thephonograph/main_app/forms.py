from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Tracklist

class TracklistForm(ModelForm):

    class Meta:
        model = Tracklist
        fields = ['track_name', 'track_duration']


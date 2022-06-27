from cProfile import label
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_age = models.IntegerField(100)
    artist_location = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name

    def get_absolute_url(self):
        return reverse('artists_detail', kwargs={"pk": self.id})



class Record(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description  = models.TextField(max_length=1000)
    format = models.CharField(max_length=50)
    release_date = models.DateField()
    image = models.URLField(max_length=1000)
    image_two = models.URLField(max_length=1000, blank=True, null=True)
    artists = models.ManyToManyField(Artist)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('records_detail', kwargs={"pk": self.id})


class Tracklist(models.Model):
    track_name = models.CharField(max_length=100)
    track_duration =models.FloatField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)



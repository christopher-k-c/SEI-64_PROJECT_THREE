from cProfile import label
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.




class Record(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description  = models.TextField(max_length=1000)
    format = models.CharField(max_length=50)
    release_date = models.DateField()
    image = models.URLField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('records_detail', kwargs={"pk": self.id})


class TrackList(models.Model):
    track_name = models.CharField(max_length=100)
    track_duration =models.FloatField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

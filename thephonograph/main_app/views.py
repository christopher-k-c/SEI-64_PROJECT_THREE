from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import TracklistForm
from .models import Record

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from.forms import TracklistForm

# Create your views here.
def home(request):
    return HttpResponse("<h1> Hello </h1>")

def about(request):
    return render(request, 'about.html')


class RecordList(ListView):
    model = Record

class RecordDetail(DetailView):
    model = Record 


class RecordCreate(CreateView):
    model = Record 
    field =  '__all__'


class RecordUpdate(UpdateView):
    model = Record
    fields = '__all__'


class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'



def add_tracklist(request, record_id):
    form = TracklistForm(request.POST)

    if form.is_valid():
        new_tracklist = form.save(commit=False)
        new_tracklist.record_id = record_id
        new_tracklist.save()
        return redirect('records_detail', record_id = record_id)

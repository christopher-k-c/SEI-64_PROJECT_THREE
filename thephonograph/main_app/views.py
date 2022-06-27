from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Record


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
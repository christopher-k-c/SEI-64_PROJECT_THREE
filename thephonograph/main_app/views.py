from ast import For
from django.shortcuts import render, redirect

from .forms import TracklistForm
from .models import Record

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .forms import TracklistForm
# User Auth Imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os

from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


class RecordList(ListView):
    model = Record

class RecordDetail(DetailView):
    model = Record
    
    def get_context_data(self, **kwargs):
        context = super(RecordDetail, self).get_context_data(**kwargs)
        context['form'] = TracklistForm()
        return context
        


class RecordCreate(LoginRequiredMixin, CreateView):
    model = Record 
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecordUpdate(LoginRequiredMixin, UpdateView):
    model = Record
    fields = '__all__'


class RecordDelete(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = '/records/'


@login_required
def add_tracklist(request, pk):
    form = TracklistForm(request.POST)

    if form.is_valid():
        new_tracklist = form.save(commit=False)
        new_tracklist.record_id = pk
        new_tracklist.save()
        return redirect('records_detail', pk = pk)


def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('records_index')
        else:
            error_message = 'Invalid Signup - Please try again later'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

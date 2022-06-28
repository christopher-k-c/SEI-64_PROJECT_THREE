from ast import For
from django.shortcuts import render, redirect

from .forms import TracklistForm
from .models import Artist, Record, Crate

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

class ArtistList(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist

class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArtistUpdate(UpdateView):
    model = Artist 
    fields = ['artist_name','artist_age','artist_location','image']   

class ArtistDelete(DeleteView):
    model = Artist   
    success_url = '/artists/'


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

# Crate Views
class CrateDetail(LoginRequiredMixin, DetailView):
    model = Crate

# Associate & Un-associate a record with a Crate
@login_required
def assoc_record(request, record_id):
    pk = request.user.id 
    Crate.objects.get(id=pk).records.add(record_id)
    return redirect('crates_detail', pk=pk)

@login_required
def unassoc_record(request, pk, record_id):
    Crate.objects.get(id=pk).records.remove(record_id)
    return redirect('crates_detail', pk=pk)


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

@login_required
def assoc_artist(request, record_id, artist_id):
    # First select object then add a toy 
    Record.objects.get(id=record_id).artist.add(artist_id)
    return redirect('detail', record_id = record_id)
@login_required
def unassoc_artist(request, record_id, artist_id):
    # Remove link from join table 
    Record.objects.get(id=record_id).artist.remove(artist_id)
    return redirect('detail', record_id = record_id)
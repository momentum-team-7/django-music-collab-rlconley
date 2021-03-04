from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ArtistForm
from .models import Album, Artist

# Create your views here.
@login_required
def index(request):
    albums = Album.objects.filter(user=request.user)
    artists = Artist.objects.all()
    return render(request, 'core/album_list.html', {'albums': albums, 'artists': artists})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'core/album_detail.html', {'album': album})

def add_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm()

    return render(request, 'core/add_artist.html', {'form': form})


def edit_artist(request, pk):
    # get the instance of the Artist model from the database
    artist = get_object_or_404(Artist, pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST, instance=artist)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'core/edit_artist.html', {'form': form, 'artist':artist })

def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/')



from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'core/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=1)
    return render(request, 'core/album_detail.html', {'album': album})

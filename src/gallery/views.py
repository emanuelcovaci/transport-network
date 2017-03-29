from django.shortcuts import render
from .models import Album, Photos
from django.core.urlresolvers import reverse

# Create your views here.


def gallery(request):
        albums = Album.objects.all()
        return render(request, 'homepages/gallery.html', context={'albums': albums})


def photos(request, album_name=None):

        album = Album.objects.get(album_name=album_name)
        album_photos = Photos.objects.filter(category_album=album).all()

        return render(request, 'homepages/photos.html', context={"photos": album_photos})

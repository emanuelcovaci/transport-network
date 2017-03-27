from django.shortcuts import render
from .models import CategoryAlbum, AlbumImage
# Create your views here.


def gallery(request):
        albums = CategoryAlbum.objects.all()
        return render(request, 'homepages/gallery.html', context={'albums': albums})


def photos(request, album_name):
        album = CategoryAlbum.objects.get(album_name=album_name)
        album_photos = AlbumImage.objects.filter(album=album).all()

        return render(request, 'homepages/photos.html', context={"photos": album_photos})

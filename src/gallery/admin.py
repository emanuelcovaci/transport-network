from django.contrib import admin
from .models import AlbumImage, CategoryAlbum

# Register your models here.

admin.site.register(AlbumImage)
admin.site.register(CategoryAlbum)
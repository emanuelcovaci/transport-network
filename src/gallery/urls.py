from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^galerie/$', views.gallery, name='gallery_page'),
    url(r'^galerie/(?P<album_name>([a-zA-Z\s])+)/fotografii/$', views.photos, name='photos_page')
]
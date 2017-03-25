from django.conf.urls import url
from . import views

app_name = "gallery"

urlpatterns = [
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^gallery/(?P<album_name>[a-zA-Z]+)/$', views.photos, name='photos')
]
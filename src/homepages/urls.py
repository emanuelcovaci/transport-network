from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^intern', views.transport_intern,name='transport_intern'),
    url(r'^adr', views.transport_adr,name='transport_adr'),
    url(r'^frigorific', views.transport_frigorific,name='transport_frigorific')
]

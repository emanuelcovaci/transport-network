# Copyright 2017-2020 Emanuel Covaci, Rares Istoc
#
# This file is part of Transport Network.
#
# Transport Network is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Transport Network is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Transport Network.  If not, see <http://www.gnu.org/licenses/>.
from django.conf.urls import url
from . import views

app_name = "homepages"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^intern', views.transport_intern, name='transport_intern'),
    url(r'^adr', views.transport_adr, name='transport_adr'),
    url(r'^frigorific', views.transport_frigorific, name='transport_frigorific'),
]

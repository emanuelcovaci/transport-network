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

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'homepages/index.html')


def transport_intern(request):
    return render(request, 'homepages/intern.html')


def transport_adr(request):
    return render(request, 'homepages/adr.html')


def transport_frigorific(request):
    return render(request, 'homepages/frigorific.html')
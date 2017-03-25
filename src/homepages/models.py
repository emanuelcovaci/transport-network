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
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class CategoryAlbum(models.Model):

    album_name = models.CharField(max_length=255, unique=True, null=False)
    album_image = models.ImageField(upload_to="./albums/" + album_name + "/",
                                    default="./albums/" + album_name + "/no-img.jpg")

    def __str__(self):
        return "{}".format(self.album_name)

    def __unicode__(self):
        return "%s" % self.album_name


class AlbumImage(models.Model):

    category_album = models.ForeignKey(CategoryAlbum, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255, unique=True, null=False)
    image_field = models.ImageField(upload_to="./albums" + category_album.album_name + "/",
                                    default="./albums" + category_album.album_name + "/no-img.jpg")

    def __str__(self):
        return "{}".format(self.image_name)

    def __unicode__(self):
        return "%s" % self.image_name

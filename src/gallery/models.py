from django.db import models
from django.conf import settings


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
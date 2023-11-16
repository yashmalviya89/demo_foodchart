# from django.db import models
# from mongoengine import Document, StringField, IntField
# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile


# # Create your models here.


# class Dish(Document):
#     dishName = StringField(required=True, max_length=100)
#     dishDesc = StringField(max_length=200)
#     dishPrice = IntField(min_value=0)
#     dishImage = models.ImageField(upload_to="dishes/", blank=True, null=True)


# # with djongo

from django.db import models
from django.contrib.auth.models import User


class Dish(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    dishName = models.CharField(max_length=100)
    dishDesc = models.CharField(max_length=200)
    dishPrice = models.IntegerField()
    dishImage = models.FileField(upload_to="dishes/", blank=True, null=True)

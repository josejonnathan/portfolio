from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='mainpage/images')
    url = models.URLField(blank=True)
    details = CharField(max_length=500, default='')

from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField


class AudioProject(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='audio_profile/images')
    url = models.URLField(blank=True)
    credits = CharField(max_length=300, default='')


class VideoGameProject(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='audio_profile/images')
    url = models.URLField(blank=True)
    credits = CharField(max_length=300, default='')


class ContactLink(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='audio_profile/images')
    url = models.URLField(blank=True)


class Features(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='audio_profile/images')
    description = CharField(max_length=300, default='')

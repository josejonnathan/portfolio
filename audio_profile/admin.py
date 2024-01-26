from django.contrib import admin
from .models import AudioProject, VideoGameProject, ContactLink, Features

admin.site.register(AudioProject)
admin.site.register(VideoGameProject)
admin.site.register(ContactLink)
admin.site.register(Features)

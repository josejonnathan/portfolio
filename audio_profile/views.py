from django.shortcuts import render
from .models import AudioProject, VideoGameProject, Features, ContactLink
# Create your views here.


def audio_profile(request):
    a_projects = AudioProject.objects.all()
    vg_projects = VideoGameProject.objects.all()
    contact = ContactLink.objects.all()
    features = Features.objects.all()
    return render(request, 'index.html', {'a_projects': a_projects, 'vg_projects': vg_projects, 'contact': contact, 'features': features})

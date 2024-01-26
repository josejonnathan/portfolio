from django.shortcuts import render
from .models import Project
# Create your views here.


def home_page(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

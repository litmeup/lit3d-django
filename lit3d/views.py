# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'lit3d/index.html')

def so(request):
    return render(request, 'lit3d/project.html')
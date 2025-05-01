# myapp/views.py
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from .models import ContactInfo, Slogans, Project, Employee

def home(request):
    return render(request, 'lit3d/index.html', context={
        "contacts": ContactInfo.objects.first(),
        "slogans": Slogans.objects.first(),
        "projects": Project.objects.filter(is_published=True),
        "employees": Employee.objects.filter(is_published=True)
    })

def so(request):
    return render(request, 'lit3d/project.html')

def projects(request, slug):
    project = Project.objects.filter(slug=slug).first()
    if not project:
        return HttpResponseNotFound()
    return HttpResponse(project.content)
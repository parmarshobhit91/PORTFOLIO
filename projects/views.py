from django.shortcuts import render
from .models import *
# Create your views here.
def project_view(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/project.html', {"all_projects": all_projects})
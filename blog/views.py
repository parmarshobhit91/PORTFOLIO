from django.shortcuts import render
from .models import *

# Create your views here.
def blog_view(request):
    internships = Internship.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'blog/blog.html', {"internships": internships, "experiences": experiences})
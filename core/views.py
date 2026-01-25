from django.shortcuts import render
from .utils import *


# Create your views here.
def home_view(request):
    return render(request, 'core/home.html')

from django.contrib.auth.models import User
from django.http import HttpResponse

def admin_creation(request):
    User.objects.create_superuser(
        username="admin",
        email="sp@example.com",
        password="admin123"
    )
    return HttpResponse("Admin created")


def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_number = request.POST.get('contact_number')

        send_email_to_me(name, email, contact_number, message)
        send_email_to_contacted_person(email)
    return render(request, 'core/contact.html')
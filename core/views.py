from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import *


# Create your views here.
def home_view(request):
    return render(request, 'core/home.html')



def about_view(request):
    return render(request, 'core/about.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_number = request.POST.get('contact_number')

        try:
            send_email_to_me(name, email, contact_number, message)
            # send_email_to_contacted_person(email)
        except Exception as e:
            # Log error but DO NOT crash
            print("Email sending failed:", e)

        messages.success(
            request,
            "Thank you for contacting me. I will get back to you shortly."
        )
        return redirect("contact")  # IMPORTANT

    return render(request, 'core/contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import *
from blog.models import Internship, Experience
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    return render(request, 'core/home.html')



def about_view(request):
    internships = Internship.objects.all()
    experiences = Experience.objects.all()
    def create_admin(request):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="bhai",
                email="youremail@gmail.com",
                password="admin123"
            )
        return HttpResponse("Admin created")
    create_admin()
    return render(request, 'core/about.html', {"internships": internships, "experiences": experiences})


from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import resend
import logging

logger = logging.getLogger(__name__)

FROM_EMAIL = "Portfolio <onboarding@resend.dev>"

def send_email_to_me(name, email, contact_number, message_text):
    if not settings.RESEND_API_KEY:
        raise ValueError("RESEND_API_KEY missing")

    resend.api_key = settings.RESEND_API_KEY

    return resend.Emails.send({
        "from": FROM_EMAIL,
        "to": ["parmarshobhit91@gmail.com"],
        "subject": "New Interest Received",
        "html": f"""
            <h3>New Contact Submission</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Contact Number:</strong> {contact_number}</p>
            <p><strong>Message:</strong><br>{message_text}</p>
        """
    })


def contact_view(request):
    if request.method == "POST":
        try:
            send_email_to_me(
                request.POST.get("name"),
                request.POST.get("email"),
                request.POST.get("contact_number"),
                request.POST.get("message"),
            )

            messages.success(
                request,
                "Thanks for contacting me! I’ll get back to you shortly."
            )

        except Exception as e:
            logger.exception("CONTACT FORM ERROR")
            print("CONTACT ERROR:", e)

            messages.error(
                request,
                "Message failed to send. Please try again later."
            )

    return render(request, "core/contact.html")

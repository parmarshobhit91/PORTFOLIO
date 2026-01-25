from django.core.mail import send_mail
from django.conf import settings

def send_email_to_me(name, email, contact_number, message_text):
    subject = "New Interest Received"
    message = f"Name : {name}, Email: {email},Contact Number: {contact_number}, Message: {message_text}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [f'{settings.EMAIL_HOST_USER}']
    send_mail(subject, message, from_email, recipient_list)

def send_email_to_contacted_person(email):
    subject = "Thank you for showing interest"
    message = f"Here is Shobhit Parmar, Software Engineer. Thank you for contacting me. I'll reach out to you shortly."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [f'{email}']
    send_mail(subject, message, from_email, recipient_list)
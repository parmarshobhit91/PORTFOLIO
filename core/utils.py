# import resend
# from django.conf import settings

# resend.api_key = settings.RESEND_API_KEY

# FROM_EMAIL = "Portfolio <onboarding@resend.dev>"  # free tier sender


# def send_email_to_me(name, email, contact_number, message_text):
#     resend.Emails.send({
#         "from": FROM_EMAIL,
#         "to": ["parmarshobhit91@gmail.com"],  # YOUR email
#         "subject": "New Interest Received",
#         "html": f"""
#             <h3>New Contact Submission</h3>
#             <p><strong>Name:</strong> {name}</p>
#             <p><strong>Email:</strong> {email}</p>
#             <p><strong>Contact Number:</strong> {contact_number}</p>
#             <p><strong>Message:</strong><br>{message_text}</p>
#         """
#     })

# This is not working due to using free service

# def send_email_to_contacted_person(email):
#     resend.Emails.send({
#         "from": FROM_EMAIL,
#         "to": [email],
#         "subject": "Thank you for showing interest",
#         "html": """
#             <p>Hi,</p>
#             <p>
#                 This is <strong>Shobhit Parmar</strong>, Software Engineer.<br>
#                 Thank you for contacting me. I’ll reach out to you shortly.
#             </p>
#             <p>Best regards,<br>Shobhit Parmar</p>
#         """
#     })

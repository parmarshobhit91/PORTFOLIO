from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="home_view"),
    path('about/', about_view, name="about_view"),
    path('contact/', contact_view, name="contact_view"),
    path('admin-create/', admin_creation)
]
from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', project_view, name="project_view"),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', blog_view, name='blog_list'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),

]
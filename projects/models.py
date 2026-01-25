from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField()
    description = models.CharField()
    github_link = models.CharField()
    live_link = models.CharField(null=True, blank=True)
    image_link = models.ImageField(upload_to='projects/')
    duration = models.CharField()



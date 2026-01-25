from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(max_length=300, null=True, blank=True)
    live_link = models.URLField(max_length=300, null=True, blank=True)
    image = CloudinaryField(
        'project_image',
        null=True,
        blank=True
        )
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    description = models.TextField(
        help_text="Use HTML <li> tags for bullet points"
    )

    image = models.ImageField(
        upload_to='experience/internships/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Internship / Training"
        verbose_name_plural = "Internships / Trainings"

    def __str__(self):
        return f"{self.title} - {self.company}"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    description = models.TextField(
        help_text="Use HTML list tags - li for bullet points"
    )

    image = models.ImageField(
        upload_to='experience/jobs/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.title} - {self.company}"

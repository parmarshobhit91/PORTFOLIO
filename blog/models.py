from django.db import models
from cloudinary.models import CloudinaryField


class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    description = models.TextField(
        help_text="Use HTML <li> tags for bullet points"
    )

    image = CloudinaryField(
        'internship_image',
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
        help_text="Use HTML <li> tags for bullet points"
    )

    image = CloudinaryField(
        'experience_image',
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


from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=300,
        help_text="Short summary shown on blog listing page"
    )

    content = models.TextField(
        help_text="Use HTML tags for formatting (p, ul, li, h2, etc.)"
    )

    cover_image = CloudinaryField(
        'blog_cover_image',
        blank=True,
        null=True
    )

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

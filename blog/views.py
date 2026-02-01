from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def blog_view(request):
    blogs = Blog.objects.filter(is_published=True)
    return render(request, 'blog/blog.html', {"blogs": blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(
        Blog,
        slug=slug,
        is_published=True
    )
    return render(request, 'blog/blog-detail.html', {'blog': blog})

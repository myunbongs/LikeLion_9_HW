from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    # blog = Blog.object.get(blog_id = id)
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    request.POST['title']
    request.POST['writer']
    request.POST['body']
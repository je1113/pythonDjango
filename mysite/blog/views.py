from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')

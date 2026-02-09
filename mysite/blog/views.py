from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': '새 글 작성'})


@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("본인의 글만 수정할 수 있습니다.")
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form.html', {'form': form, 'title': '글 수정'})


@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("본인의 글만 삭제할 수 있습니다.")
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/delete.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')

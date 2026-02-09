from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # DB 저장 전 객체만 생성
            post.author = request.user       # 현재 로그인 사용자를 작성자로
            post.save()
            return redirect('detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': '새 글 작성'})


def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # 기존 데이터에 덮어쓰기
        if form.is_valid():
            form.save()
            return redirect('detail', post_id=post.id)
    else:
        form = PostForm(instance=post)  # 기존 데이터를 폼에 채워서 보여줌
    return render(request, 'blog/form.html', {'form': form, 'title': '글 수정'})


def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/delete.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')

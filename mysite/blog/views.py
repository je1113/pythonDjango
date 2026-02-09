from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>블로그 홈페이지</h1><p>첫 번째 Django View입니다!</p>")


def about(request):
    return HttpResponse("<h1>소개 페이지</h1><p>Django 학습 중입니다.</p>")

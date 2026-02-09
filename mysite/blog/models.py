from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)           # 제목
    content = models.TextField()                        # 본문
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일 (자동)
    updated_at = models.DateTimeField(auto_now=True)      # 수정일 (자동)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # 최신 글이 먼저

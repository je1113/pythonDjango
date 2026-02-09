from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']  # 목록에 표시할 컬럼
    list_filter = ['created_at', 'author']             # 필터 사이드바
    search_fields = ['title', 'content']               # 검색 가능 필드

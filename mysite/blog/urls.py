from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                # /blog/
    path('<int:post_id>/', views.detail, name='detail'), # /blog/1/
    path('about/', views.about, name='about'),           # /blog/about/
]

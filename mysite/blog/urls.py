from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                       # /blog/
    path('create/', views.create, name='create'),              # /blog/create/
    path('<int:post_id>/', views.detail, name='detail'),       # /blog/1/
    path('<int:post_id>/update/', views.update, name='update'),  # /blog/1/update/
    path('<int:post_id>/delete/', views.delete, name='delete'),  # /blog/1/delete/
    path('about/', views.about, name='about'),                 # /blog/about/
]

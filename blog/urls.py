from django.urls import path
from .views import posts_render, post_detail

app_name = 'blog'

urlpatterns = [
    path('', posts_render, name='post'),
    path('<int:post_id>', post_detail, name='post_detail'),
    
]
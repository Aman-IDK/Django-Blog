from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('posts/new/', PostCreateView.as_view(), name = 'post-create'),
    path('about/', views.about, name = 'blog-about'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),

]    


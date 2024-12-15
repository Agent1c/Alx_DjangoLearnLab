# accounts/urls.py

from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Blog Post Management Features
    path('posts/',PostListView.as_view(), name='blogpost-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='blogpost-detail'),
    path('posts/new/', PostCreateView.as_view(), name='blogpost-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='blogpost-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blogpost-delete'),
]

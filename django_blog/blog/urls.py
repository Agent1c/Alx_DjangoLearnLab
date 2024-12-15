# accounts/urls.py

from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import TaggedPostListView, register, user_login, user_logout, profile, PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView,PostByTagListView, search

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Blog Post Management Features
    path('post/',PostListView.as_view(), name='blogpost-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blogpost-detail'),
    path('post/new/', PostCreateView.as_view(), name='blogpost-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blogpost-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blogpost-delete'),

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    path('search/', search, name='search'),
    path('tags/<str:tag_name>/', TaggedPostListView.as_view(), name='tagged_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name="posts_by_tag"),
]

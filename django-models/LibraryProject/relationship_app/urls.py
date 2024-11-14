from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("templates/",views.book_list, name='book_list'),
    path('', views.index, name='index'),
    path('about/', views.about),

]

from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Articles


urlpatterns = [
    path('', views.news_home, name='news_home'),
]

from django.shortcuts import render, redirect
from .models import Articles


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/posts.html', {'news': news})

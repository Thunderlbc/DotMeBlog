# -*-coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from article.models import Articles
from datetime import datetime
# Create your views here.


def detail(request, id):
    try:
        post = Articles.objects.get(id=str(id))
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def home(request):
    post_list = Articles.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def archives(request):
    post_list = Articles.objects.all().order_by('-date_time')
    return render(request, 'archives.html', {'post_list': post_list})



def search_tag(request, tag):
    try:
        post_list = Articles.objects.filter(category_iexact=tag)
    except Articles.DoesNotExist:
        raise Http404
    return render(request, 'tag.html')

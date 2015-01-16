from django.shortcuts import render
from django.http import HttpResponse
from article.models import Articles
from datetime import datetime
# Create your views here.


def home(request):
    return HttpResponse("Hello World, Django!")


def detail(request, my_args):
    post = Articles.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)


def home(request):
    post_list = Articles.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

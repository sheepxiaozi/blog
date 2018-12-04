from django.shortcuts import render
from article.models import Article
from django.http import Http404


def index(request):
    post_list = Article.objects.all()
    return render(request, "index.html", {"post_list": post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})



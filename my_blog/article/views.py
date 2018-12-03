from django.shortcuts import render
from article.models import Article


def index(request):
    post_list = Article.objects.all()
    return render(request, "index.html", {"post_list": post_list})



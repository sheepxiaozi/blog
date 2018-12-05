from django.shortcuts import render, redirect
from article.models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed


def index(request):
    post_list = Article.objects.all()
    return render(request, "index.html", {"post_list": post_list})


def detail(request, pk):
    try:
        post = Article.objects.get(id=str(pk))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'index.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content



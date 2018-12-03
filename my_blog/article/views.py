from django.http import HttpResponse
from article.models import Article


def index(request):
    return HttpResponse("Hello World")


def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    data = "title = %s, category = %s, date_time = %s, content = %s"\
           % (post.title, post.category, post.date_time, post.content)
    return HttpResponse(data)




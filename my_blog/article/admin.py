from django.contrib import admin
from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time')
    search_fields = ('title', 'category', 'content')
    list_filter = ("date_time",)
    date_hierarchy = 'date_time'

admin.site.register(Article, ArticleAdmin)


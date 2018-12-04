from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_article'  # 指明数据库表名
        verbose_name = '博客'
        verbose_name_plural = verbose_name
        ordering = ['-date_time']  # 按时间下降排序


class Comment(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=True, verbose_name='博客')

    class Meta:
        db_table = 'tb_comment'
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]



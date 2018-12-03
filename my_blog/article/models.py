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
        ordering = ['-date_time']  # 按时间下降排序



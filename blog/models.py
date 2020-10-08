# -*- coding=utf-8 -*-


from django.db import models


# Create your models here.


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    # 标题
    title = models.TextField()
    # 预览
    brief_content = models.TextField()
    # 内容
    content = models.TextField()
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

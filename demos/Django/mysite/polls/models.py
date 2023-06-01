import datetime

from django.db import models
from django.utils import timezone

"""
每个模型被表示为 django.db.models.Model 类的子类。
每个模型有许多类变量，它们都表示模型里的一个数据库字段。

每个字段都是 Field 类的实例
- 比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。
这将告诉 Django 每个字段要处理的数据类型。
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # 我们使用 ForeignKey 定义了一个关系。
    # 这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

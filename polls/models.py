from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# 1.CharField : 字符串字段
#       有两个参数，max_length:必需的，字段的最大长度。db_collation：可选的，字段的数据库排序规则名称。
# 2.DateTimeField ： 日期和时间（python中的datetime.datetime)
#       与DateField（日期，datetime.date）有相同的参数:
#               auto_now:每次保存对象时自动将字段设置为现在
#               auto_now_add:

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)  # 设置字段名
#     last_name = models.CharField(max_length=30)
# 相当于创建了一个：
# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,  id字段自动添加
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_text

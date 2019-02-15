from django.db import models

# Create your models here.
from blog_user.models import Buser


class Comment(models.Model):
    choice = (
        (1,"回复"),
              (2,"评论")
              )
    context = models.TextField(max_length=200,verbose_name="评论内容")
    user_tel = models.CharField(max_length=20,verbose_name="用户手机号")
    content_id = models.CharField(max_length=10,verbose_name="文章ID")
    parent_id = models.SmallIntegerField(choices=choice,default=2)
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.context
    class Meta:

        verbose_name="评论管理"
        verbose_name_plural=verbose_name

from django.db import models

# Create your models here.
from blog_user.models import Buser
from db.base_model import BaseModel


class Liuyan(BaseModel):
    choice = ((1,"回复"),(2,"留言"))
    context = models.TextField(max_length=200,verbose_name="留言内容")
    user_tel = models.CharField(max_length=20,verbose_name="用户手机号")
    content_id = models.CharField(max_length=10,verbose_name="文章ID")
    parent_id = models.SmallIntegerField(choices=choice,default=2)

    def __str__(self):
        return self.context
    class Meta:
        db_table='Bconment'
        verbose_name="留言管理"
        verbose_name_plural=verbose_name

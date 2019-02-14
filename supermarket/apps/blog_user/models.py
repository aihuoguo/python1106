from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

# Create your models here.
from db.base_model import BaseModel


class Buser(BaseModel):
    choice = (
        (1,"不能留言"),
        (2,"不能登录"),
        (3,"正常")
    )
    username = models.CharField(max_length=20,verbose_name="粉丝名")
    tel = models.CharField(max_length=11,validators=[RegexValidator(r'1[35678]\d{9}')],verbose_name="用户号码")
    password = models.CharField(max_length=32,validators=[MinLengthValidator(6)],verbose_name="用户密码")
    status = models.SmallIntegerField(choices=choice,default=3,verbose_name="状态")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除")
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    head = models.ImageField(upload_to="fans/%Y%m",default="head/icon4.png",verbose_name="用户头像")
    score = models.IntegerField(default=6666,verbose_name="积分")

    def __str__(self):
        return self.tel
    class Meta:
        db_table="Buser"
        verbose_name="粉丝管理"
        verbose_name_plural = verbose_name
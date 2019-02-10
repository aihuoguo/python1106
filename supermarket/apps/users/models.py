from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


# Create your models here.
# 个人资料表
from db.base_model import BaseModel


class Users(models.Model):
    sex_choices = (
        (1, "男"),
        (2, "女"),
    )
    # 手机号
    username = models.CharField(max_length=20,
                                validators=[
                                    MinLengthValidator(11, '用户名为11位')
                                ])
    # 密码
    password = models.CharField(max_length=32)
    # 用户名
    tel = models.CharField(max_length=50,
                                null=True,
                                blank=True,
                                )
    # 性别
    sex = models.SmallIntegerField(choices=sex_choices,
                                   default=1,
                                   )
    # 学校
    school_name = models.CharField(max_length=50,
                                   null=True,
                                   blank=True,
                                   )
    # 家乡
    hometown = models.CharField(max_length=50,
                                null=True,
                                blank=True,
                                )
    # 生日
    birth_time = models.DateField(null=True,
                                  blank=True,
                                  )
    # 详细地址
    address = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               )
    #头像
    logo = models.ImageField(upload_to='shop/%Y%m/%d',
                             default='head/memtx.png',
                             verbose_name='店铺LOGO')

    # 是否删除
    is_delete = models.BooleanField(default=False)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name='用户管理'
        verbose_name_plural=verbose_name


class UserAddress(BaseModel):
    """用户收货地址管理"""
    user = models.ForeignKey(to="Users", verbose_name="创建人")
    username = models.CharField(verbose_name="收货人", max_length=100)
    phone = models.CharField(verbose_name="收货人电话",
                             max_length=11,
                             validators=[
                                 RegexValidator('^1[3-9]\d{9}$', '电话号码格式错误')
                             ])
    hcity = models.CharField(verbose_name="省", max_length=100, blank=True, null=True)
    hproper = models.CharField(verbose_name="市", max_length=100, blank=True, null=True)
    harea = models.CharField(verbose_name="区", max_length=100)
    brief = models.CharField(verbose_name="详细地址", max_length=255)
    isDefault = models.BooleanField(verbose_name="是否设置为默认", default=False)

    class Meta:
        verbose_name = "收货地址管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.username,self.phone)


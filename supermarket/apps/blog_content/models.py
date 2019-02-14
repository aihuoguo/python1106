from django.db import models

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=20,verbose_name="分类标题")
    brief = models.TextField(max_length=200,verbose_name="简介")
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.cat_title
    class Meta:
        db_table = "Bcat"
        verbose_name="文章分类管理"
        verbose_name_plural=verbose_name





class Docket(models.Model):
    doc_title = models.CharField(max_length=20,verbose_name="标签名字")
    brief = models.TextField(max_length=200,verbose_name="简介")

    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")

    def __str__(self):
        return self.doc_title
    class Meta:
        db_table = "Biaoqian"
        verbose_name="标签管理"
        verbose_name_plural=verbose_name


class ContentModle(models.Model):
    choice=(
        (1,"发表"),
            (2,"未发表")
    )
    con_title = models.CharField(max_length=20,verbose_name="文章标题")
    brief = models.TextField(max_length=200,verbose_name="内容",null=True)
    category = models.ForeignKey(to=Category,verbose_name="文章分类")
    docket = models.ForeignKey(to=Docket,verbose_name="标签")
    status = models.SmallIntegerField(choices=choice,default=1)
    score = models.DecimalField(max_digits=9,verbose_name="所需积分",decimal_places=2,default=0)
    add_time = models.DateField(auto_now_add=True,verbose_name="添加时间")
    update_time = models.DateField(auto_now=True,verbose_name="更新时间")
    is_delete = models.BooleanField(default=True,verbose_name="是否删除")
    def __str__(self):
        return self.con_title
    class Meta:
        db_table = "Bcon"
        verbose_name="文章内容管理"
        verbose_name_plural=verbose_name






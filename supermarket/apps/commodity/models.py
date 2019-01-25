from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

from db.base_model import BaseModel


# 商品类型表
class GoodsType(BaseModel):
    type_name = models.CharField(max_length=50, verbose_name='商品类名')
    sort_detail = models.TextField(verbose_name='分类详情')
    order = models.SmallIntegerField(default=0, verbose_name="排序")

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'goodstype'
        verbose_name = '商品类型表管理'
        verbose_name_plural = verbose_name


# 商品SPU表
class GoodsSPU(BaseModel):
    spu_name = models.CharField(max_length=50, verbose_name='SPU名')
    spu_detail = RichTextUploadingField(verbose_name='SPU简介')

    def __str__(self):
        return self.spu_name

    class Meta:
        db_table = 'goodsspu'
        verbose_name = '商品SPU表管理'
        verbose_name_plural = verbose_name


# 单位表
class Unit(BaseModel):
    unit_name = models.CharField(max_length=50, verbose_name='单位名')

    def __str__(self):
        return self.unit_name

    class Meta:
        db_table = 'unit'
        verbose_name = '单位表管理'
        verbose_name_plural = verbose_name


# 商品SKU表
class GoodsSKU(BaseModel):
    sku_name = models.CharField(max_length=50, verbose_name='SKU')
    brief = models.TextField(verbose_name='SKU简介')
    price = models.DecimalField(verbose_name='价格',
                                max_digits=9,
                                decimal_places=2,
                                default=0,
                                )
    unit = models.CharField(max_length=10, verbose_name='单位')
    stock = models.IntegerField(verbose_name='库存')
    sales_val = models.IntegerField(verbose_name='销量')
    logo = models.ImageField(verbose_name='封面图片', upload_to='goods/%Y%m/%d')

    res = ((False, "下架"), (True, "上架"))
    is_on_sale = models.BooleanField(verbose_name='是否上架', choices=res, default=False)
    goods_type = models.ForeignKey(to='GoodsType', verbose_name='商品分类id')
    goods_spu = models.ForeignKey(to='GoodsSPU', verbose_name='商品SPU_id')

    def __str__(self):
        return self.sku_name

    class Meta:
        db_table = 'goodssku'
        verbose_name = '商品SKU表管理'
        verbose_name_plural = verbose_name


# 商品相册
class GoodsPhoto(BaseModel):
    img_url = models.ImageField(verbose_name='相册图片地址', upload_to='goods_gallery/%Y%m/%d')
    goods_sku = models.ForeignKey(to="GoodsSKU", verbose_name="商品SKU")

    def __str__(self):
        return "商品相册:{}".format(self.img_url.name)

    class Meta:
        verbose_name = "商品相册管理"
        verbose_name_plural = verbose_name


# 商品轮播表
class Carousel(BaseModel):
    name = models.CharField(max_length=200, verbose_name='轮播活动名')
    img_url = models.ImageField(verbose_name='轮播图片地址', upload_to='carousel/%Y%m/%d')
    order = models.SmallIntegerField(verbose_name="排序",
                                     default=0,
                                     )

    goods_sku = models.ForeignKey(to="GoodsSKU", verbose_name="商品SKU")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "轮播管理"
        verbose_name_plural = verbose_name


# 首页活动表
class Activity(BaseModel):
    act_name = models.CharField(max_length=50, verbose_name='活动名')
    img_url = models.ImageField(verbose_name='活动图片地址', upload_to='activity/%Y%m/%d')
    url_address = models.URLField(verbose_name='活动的url地址', max_length=200)

    def __str__(self):
        return self.act_name

    class Meta:
        db_table = 'activity'
        verbose_name = '活动管理'
        verbose_name_plural = verbose_name


# 首页活动专区
class Activity_Area(BaseModel):
    name = models.CharField(verbose_name='活动专区名称', max_length=100)
    describe = models.TextField(verbose_name='专区的描述')

    res = ((False, "下架"), (True, "上架"))
    is_on_sale = models.BooleanField(verbose_name='是否上架', choices=res, default=False)
    goods_sku = models.ManyToManyField(to="GoodsSKU", verbose_name="商品")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "活动专区管理"
        verbose_name_plural = verbose_name

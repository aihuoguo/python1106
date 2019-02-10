from django.db import models

# Create your models here.
from django.db import models

from db.base_model import BaseModel


class Transport(BaseModel):
    """运算方式"""
    name = models.CharField(max_length=50, verbose_name="运输方式")
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='运费')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "运输方式管理"
        verbose_name_plural = verbose_name


class Order(BaseModel):
    """订单基本信息表"""
    order_status_choices = (
        (0, "未支付"),
        (1, "已支付"),
        (2, "已发货"),
        (3, "未评价"),
        (4, "已完成"),
        (5, "退发货"),
        (6, "取消订单"),
    )
    user = models.ForeignKey(to="users.Users", verbose_name="用户")
    order_sn = models.CharField(max_length=64, verbose_name="订单编号")
    goods_total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name="商品总金额")
    transport_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="运费")
    transport = models.CharField(max_length=50, verbose_name="运输方式")
    username = models.CharField(max_length=50, verbose_name="收货人姓名")
    phone = models.CharField(max_length=11, verbose_name="收货人电话号码")
    address = models.CharField(max_length=250, verbose_name="收货人地址")
    order_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name="订单总金额")
    order_status = models.SmallIntegerField(choices=order_status_choices, default=0, verbose_name="订单状态")
    payment = models.ForeignKey(to="Payment", null=True, blank=True, verbose_name="支付方式")

    pay_time = models.DateTimeField(verbose_name="支付时间", null=True, blank=True)
    deliver_time = models.DateTimeField(verbose_name="发货时间", null=True, blank=True)
    finish_time = models.DateTimeField(verbose_name="完成时间", null=True, blank=True)

    def __str__(self):
        return self.order_sn

    class Meta:
        verbose_name = "订单管理"
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    """订单商品详情表"""
    order = models.ForeignKey(to="Order", verbose_name="订单ID")
    goods_sku = models.ForeignKey(to="commodity.GoodsSKU", verbose_name="订单商品ID")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="商品价格")
    count = models.SmallIntegerField(verbose_name="订单商品数量")

    def __str__(self):
        return "{}:{}".format(self.order.order_sn, self.goods_sku.sku_name)

    class Meta:
        verbose_name = "订单商品管理"
        verbose_name_plural = verbose_name


class Payment(BaseModel):
    name = models.CharField(max_length=50, verbose_name="支付方式")
    brief = models.CharField(max_length=200, verbose_name="说明")
    logo = models.ImageField(upload_to="payment/%Y", verbose_name="支付LOGO")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "支付方式管理"
        verbose_name_plural = verbose_name

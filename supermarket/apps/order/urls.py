from django.conf.urls import url

from order.views import allorder, order, orderdetail, pay

urlpatterns = [
    url(r'^allorder/$',allorder,name='allorder'), # 全部订单
    url(r'^order/$',order,name='order'), # 确认订单
    url(r'^orderdetail/$',orderdetail,name='orderdetail'), # 订单详情
    url(r'^pay/$',pay,name='pay'), # 支付页面

]
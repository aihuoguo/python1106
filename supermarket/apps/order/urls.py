from django.conf.urls import url

from order.views import ConOrder, ShowOrder, Pay

urlpatterns = [
    # url(r'^allorder/$',allorder,name='allorder'), # 全部订单
    url(r'^conorder/$',ConOrder.as_view(),name='确认订单'), # 确认订单
    url(r'^showorder/$',ShowOrder.as_view(),name='确认支付'),
    url(r'^pay/$',Pay.as_view(),name='展示支付'),

]
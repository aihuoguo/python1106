from django.conf.urls import url

from order.views import ConOrder, ShowOrder

urlpatterns = [
    # url(r'^allorder/$',allorder,name='allorder'), # 全部订单
    url(r'^conorder/$',ConOrder.as_view(),name='确认订单'), # 确认订单
    url(r'^showorder/$',ShowOrder.as_view(),name='确认支付'),

]
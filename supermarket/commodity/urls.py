from django.conf.urls import url

from commodity.views import index, category, detail

urlpatterns = [
    url(r'^index/$',index,name='index'), # 首页
    url(r'^detail/$',detail,name='detail'), # 商品详情
    url(r'^category/$',category,name='category'), # 超市商品列表
]
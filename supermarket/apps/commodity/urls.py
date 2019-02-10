from django.conf.urls import url

from commodity.views import DetailView, TypeView, IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^type/(?P<cate_id>\d*)_{1}(?P<order>\d?)\.html$',TypeView .as_view(), name='商品类型'),
    url(r'^detail/(?P<id>\d+)/$', DetailView.as_view(), name='商品详情'),
]
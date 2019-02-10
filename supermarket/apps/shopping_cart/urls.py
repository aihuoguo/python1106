from django.conf.urls import url

from shopping_cart.views import AddCartView,CartListView

urlpatterns = [
    url(r'^add/$',AddCartView.as_view(),name='添加购物车'),
    url(r'^list/$',CartListView.as_view(),name='购物车列表'),
]
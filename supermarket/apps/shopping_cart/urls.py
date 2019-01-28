from django.conf.urls import url

from shopping_cart.views import AddCartView, DelCartView, CartView

urlpatterns = [
    url(r'^add/$',AddCartView.as_view(),name='添加购物车'),
    url(r'^del/$',DelCartView.as_view(),name='减少购物车'),
    url(r'^cart/$',CartView.as_view(),name='cart'),
]
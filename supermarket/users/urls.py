from django.conf.urls import url

from users.views import member, login, reg

urlpatterns = [
    url(r'^member/$',member,name='member'), #  个人中心
    url(r'^login/$',login,name='login'), # 登录
    url(r'^reg/$',reg,name='reg'), # 注册

]
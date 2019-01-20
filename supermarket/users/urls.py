from django.conf.urls import url

from users.views import member, login, reg, RegisterView, LoginView, info

urlpatterns = [
    url(r'^member/$',member,name='member'), #  个人中心
    # url(r'^login/$',login,name='login'), # 登录
    # url(r'^reg/$',reg,name='reg'), # 注册
    url(r'register/$',RegisterView.as_view(),name='注册'),
    url(r'login/$',LoginView.as_view(),name='登录'),
    url(r'info/$',info,name='个人资料'),

]
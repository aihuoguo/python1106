from django.conf.urls import url

from blog_user.views import RegisterView, LoginView, MemberView, FsMsgView

urlpatterns = [
    url(r'register/$', RegisterView.as_view(), name='注册'),
    url(r'login/$', LoginView.as_view(), name='登录'),
    url(r'menber/$', MemberView.as_view(), name='个人中心'),
    url(r'famsg/$', FsMsgView.as_view(), name='发送短信'),
    ]
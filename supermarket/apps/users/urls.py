from django.conf.urls import url

from users.views import RegisterView, LoginView, InfoView, MemberView, forget_pwd, safe, FsMsgView, UpdatePwdView, \
    AddressList, Address

urlpatterns = [
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'info/$', InfoView.as_view(), name='info'),
    url(r'member/$', MemberView.as_view(), name='member'),
    url(r'FsMsg/$', FsMsgView.as_view(), name='FsMsg'),
    url(r'forget_pwd/$', forget_pwd, name='forget_pwd'),
    url(r'safe/$', safe, name='safe'),
    url(r'updatepwd/$', UpdatePwdView.as_view(), name='updatepwd'),
    url(r'address/$', Address.as_view(), name='address'),
    url(r'addresslist/$', AddressList.as_view(), name='addresslist'),

]

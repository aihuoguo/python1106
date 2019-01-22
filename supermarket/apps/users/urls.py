from django.conf.urls import url

from users.views import RegisterView, LoginView, InfoView, MemberView, forget_pwd, safe, xiugaipwd, FsMsgView

urlpatterns = [
    url(r'register/$',RegisterView.as_view(),name='register'),
    url(r'login/$',LoginView.as_view(),name='login'),
    url(r'info/$',InfoView.as_view(),name='info'),
    url(r'member/$',MemberView.as_view(),name='member'),
    url(r'FsMsg/$',FsMsgView.as_view(),name='FsMsg'),
    url(r'forget_pwd',forget_pwd,name='forget_pwd'),
    url(r'safe',safe,name='safe'),
    url(r'xiugaipwd',xiugaipwd,name='xiugaipwd'),

]
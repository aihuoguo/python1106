from django.conf.urls import url

from blog_liuyan.views import comment

urlpatterns = [
    url(r'^comment/',comment, name="评论"),
]
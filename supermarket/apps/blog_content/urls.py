from django.conf.urls import url

from blog_content.views import index, detail, category, label

urlpatterns = [
    url(r'^index/',index,name="主页"),
    url(r'^detail/(?P<id>\d+)', detail, name="详情"),
    url(r'^category/(?P<cate_id>\d+)', category, name="分类"),
    url(r'^label/(?P<doc_id>\d+)', label, name="标签"),

]
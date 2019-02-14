from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from blog_content.models import Category, ContentModle, Docket
from blog_liuyan.models import Liuyan
from blog_user.models import Buser

#主页
def index(request):
    if request.session.get("id") is None:
        return redirect(reverse("博客用户:登录"))
    #获取用户ID
    id = request.session.get("id")

    user = Buser.objects.get(pk=id)
    #获取所有分类
    category = Category.objects.all()


    content = ContentModle.objects.filter(status=1)
    docket = Docket.objects.all()

    #paginator实现分页
    paginator = Paginator(content,2)
    page = request.GET.get("page",1)
    #获取当前页码
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        #页面不是数据
        content = paginator.page(1)
    except EmptyPage:
        #页码为空，显示最后一页
        content = paginator.page(paginator.num_pages)

    context = {"user":user,"category":category,"content":content,"docket":docket,}
    return render(request,"blog_content/index.html",context=context)



#详情
def detail(request,id):
    if request.session.get("id") is None:
        return redirect(reverse("博客用户:登录"))

    #获取文章
    content = ContentModle.objects.get(pk=id)
    #获取分类

    #获取缓存中的用户ID
    bid = request.session.get("id")
    #获取用户信息
    user = Buser.objects.get(pk=bid)
    #获取对呀文章的ID
    con_id=id
    #获取文章评论
    comment = Liuyan.objects.filter(content_id=con_id,is_delete=True)
    context = {"content":content,"user":user,"con_id":con_id,"comment":comment}
    return render(request,"blog_content/detail.html",context=context)


#分类查询
def category(request,cate_id):
    if request.session.get("id") is None:
        return redirect(reverse("博客用户:登录"))
    # 获取缓存中的用户ID
    bid = request.session.get("id")
    # 获取用户信息
    user = Buser.objects.get(pk=bid)
    category = Category.objects.all()
    cate_gory=Category.objects.get(pk=cate_id)
    content = ContentModle.objects.filter(category=cate_id)
    context = {"content":content,"category":category,"user":user,"cate_gory":cate_gory}
    return render(request,"blog_content/caty.html",context=context)

def label(request,doc_id):
    if request.session.get("id") is None:
        return redirect(reverse("博客用户:登录"))
    #获取用户ID
    id = request.session.get("id")
    #获取用户信息
    user = Buser.objects.get(pk=id)
    #获取所有分类
    category = Category.objects.all()
    #获取标签下的内容
    content = ContentModle.objects.filter(docket=doc_id)
    #获取所有标签
    docket = Docket.objects.all()
    #获取选标签名字
    title = Docket.objects.get(pk=doc_id)
    context = {"user":user,
               "category":category,
               "docket":docket,
               "content":content,
               "title":title}
    return render(request,"blog_content/label.html",context=context)


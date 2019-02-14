import random
import uuid
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from blog_user import set_password
from blog_user.forms import RegformModel, LoginformModel
from blog_user.helper import check_bloglogin
from blog_user.models import Buser
import re
from django_redis import get_redis_connection

from users.helper import send_sms, check_login


class RegisterView(View):  # 注册

    def get(self, request):
        # 展示登录表单
        return render(request, 'blog_user/reg.html')

    def post(self, request):
        # 注册
        # 接收参数
        data = request.POST
        # 验证是否合法
        form = RegformModel(data)
        if form.is_valid():
            # 操作数据库
            # 获取清洗数据
            cleaned_data = form.cleaned_data
            # 创建用户
            user = Buser()
            user.tel = cleaned_data.get("tel")
            user.password = set_password(cleaned_data.get("password"))
            user.save()
            # 跳转页面
            return redirect('博客用户:登录')
        else:
            # 合成响应
            context = {"errors": form.errors}
            return render(request, "blog_user/reg.html", context=context)


class LoginView(View):  # 登录
    def get(self, request):
        return render(request, 'blog_user/login.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 验证数据的合法性
        form = LoginformModel(data)
        if form.is_valid():
            #接受参数
            #将数据保存到seeion中
            user = form.cleaned_data.get("user")
            request.session["id"] = user.pk
            request.session["tel"] = user.tel
            request.session["head"] = user.head
            request.session["status"] = user.status
            request.session.set_expiry(0)#关闭浏览器就消失
            return redirect(reverse("博客内容:主页"))
            # return redirect(reverse("blog_content:主页"))
        else:
            context={"errors":form.errors}
            return render(request,"blog_user/login.html",context=context)


# 个人中心
class MemberView(View):
    @method_decorator(check_bloglogin)
    def get(self, request):
        return render(request, 'blog_user/mine.html')

    @method_decorator(check_bloglogin)
    def post(self, request):
        pass


# 发送短信验证注册
class FsMsgView(View):
    def get(self,request):
        pass
    def post(self,request):
        tel = request.POST.get("tel")
        rs = re.search("^1[3-9]\d{9}$", tel)
        if rs is None:
            return JsonResponse({"errrors": 1, "errmsg": "手机号码错误"})
        random_code = "".join([str(random.randint(0, 9)) for _ in range(4)])
        print("========验证码为{}======".format(random_code))
        # 获取redis连接
        r = get_redis_connection()
        # 保存验证码
        r.set(tel, random_code)
        # 验证码60S后过期
        r.expire(tel, 60)
        # 创建次数变量
        key_time = "{}_times".format(tel)
        # 获取当前次数
        now_time = r.get(key_time)
        if now_time is None or int(now_time) <= 10:
            r.incr(key_time)
            r.expire(key_time, 3600)
        else:
            return JsonResponse({"errors": 1, "errmsg": "发送次数过多，稍后再试"})

        return JsonResponse({"errors": 0})

            # __business_id = uuid.uuid1()
            # params = "{\"code\":\"%s\",\"product\":\"跳舞的兔子\"}" % yz_cade
            # # print(params)
            # rs = send_sms(__business_id, tel, "注册验证", "SMS_2245271", params)
            # print(rs.decode('utf-8'))

import random
import re
import uuid

from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django_redis import get_redis_connection

from db.base_view import VerifyLoginView

from users import set_password
from users.forms import RegisterModelForm, LoginModelForm, InfoModelForm
from users.helper import login, check_login, send_sms
from users.models import Users


class RegisterView(View):  # 注册

    def get(self, request):
        # 展示登录表单
        return render(request, 'users/reg.html')

    def post(self, request):
        # 注册
        # 接收参数
        data = request.POST
        # 验证是否合法
        form = RegisterModelForm(data)
        if form.is_valid():
            # 操作数据库
            # 获取清洗数据
            cleaned_data = form.cleaned_data
            # 创建用户
            user = Users()
            user.username = cleaned_data.get('username')
            user.password = set_password(cleaned_data.get('password'))
            user.save()
            # 跳转页面
            return redirect('用户:login')
        else:
            # 合成响应
            return render(request, 'users/reg.html', context={'form': form})


class LoginView(View):  # 登录
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 验证数据的合法性
        form = LoginModelForm(data)
        if form.is_valid():
            # 操作数据库
            # 保存登录标识到session中
            user = form.cleaned_data['user']
            login(request, user)
            # 合成响应
            return redirect('用户:member')
        else:
            # 合成响应
            return render(request, 'users/login.html', {'form': form})


# 个人中心
class MemberView(View):
    @method_decorator(check_login)
    def get(self, request):
        return render(request, 'users/member.html')

    @method_decorator(check_login)
    def post(self, request):
        pass



# 个人资料
class InfoView(View):
    def get(self, request):
        return render(request, 'users/infor.html')
    def post(self, request):
        # 接受参数
        data = request.POST
        form = InfoModelForm(data)
        # 验证是否合法
        if form.is_valid():
            # 操作数据库
            # 获取清洗数据
            cleaned_data = form.cleaned_data
            # 更新
            Users.objects.filter(pk=id).update(username=cleaned_data.get('username'),
                                               tel=cleaned_data.get('tel'),
                                               birth_time=cleaned_data.get('birth_time'),
                                               sex=cleaned_data.get('sex'),
                                               school_name=cleaned_data.get('school_name'),
                                               location=cleaned_data.get('location'),
                                               hometown=cleaned_data.get('hometown'),
                                               password=set_password(cleaned_data.get('password')
                                                                     )
                                               )
            # 跳转页面
            return redirect('用户:member')
        else:
            # 合成响应
            return render(request, 'users/infor.html', context={'form': form})



def forget_pwd(request):
    return render(request,'users/forgetpassword.html')

def safe(request):
    return render(request,'users/saftystep.html')

def xiugaipwd(request):
    return render(request, 'users/password.html')


class FsMsgView(View):
    def get(self,request):
        pass
    def post(self,request):
        # 接受参数 手机号码
        username=request.POST.get('username','')
        # 验证格式
        res=re.search('^1[3-9]\d{9}',username)
        if res is None:
            #如果格式不正确返回错误信息
            return JsonResponse({'error':1,'errormsg':'手机号码格式错误'})
        else:
            #生成随机数字字符串
            yz_cade=''.join(str(random.randint(0,9))for r in range(1,6))
            print('***********随机验证码为*{}**************'.format(yz_cade))
            #保存验证码到redis
            #获取连接
            r=get_redis_connection()
            #保存对应的手机验证码
            r.set(username,yz_cade)
            r.expire(username,60)
            #当前手机号验证码的次数
            key_times='{}_times'.format(username)
            now_times=r.get(key_times)
            #保存手机发送验证码的次数
            if now_times is None or int(now_times) < 5:
                r.incr(key_times)
                #设置一个过期事件
                r.expire(username,10)
            else:
                return JsonResponse({'error':1,'errmsg':'发送次数过多'})

            __business_id = uuid.uuid1()
            params = "{\"code\":\"%s\",\"product\":\"跳舞的兔子\"}" % yz_cade
            # print(params)
            rs = send_sms(__business_id, username, "注册验证", "SMS_2245271", params)
            print(rs.decode('utf-8'))
            return JsonResponse({'error':0})



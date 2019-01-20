from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from users import set_password
from users.forms import RegisterModelForm, LoginModelForm
from users.models import Users


def member(repuest):  # 个人中心
    return render(repuest,'users/member.html')

def info(request): #个人资料
    return HttpResponse('ok')

def login(repuest): # 登录
    return render(repuest,'users/login.html')

def reg(repuest): # 注册
    return render(repuest,'users/reg.html')

class RegisterView(View):# 注册

    def get(self,request):
        #展示登录表单
        return render(request,'users/reg.html')
    def post(self,request):
        #注册
        #接收参数
        data=request.POST
        #验证是否合法
        form=RegisterModelForm(data)
        if form.is_valid():
            # 操作数据库
            #获取清洗数据
            cleaned_data = form.cleaned_data
            # 创建用户
            user = Users()
            user.username = cleaned_data.get('username')
            user.password = set_password(cleaned_data.get('password'))
            user.save()
            #跳转页面
            return redirect('用户:login')
        else:
            #合成响应
            return render(request,'users/reg.html',context={'form':form})

class LoginView(View): #登录
    def get(self,request):
        return render(request,'users/login.html')

    def post(self,request):
        # 接收参数
        data = request.POST

        # 验证数据的合法性
        form = LoginModelForm(data)
        if form.is_valid():
            # 验证成功
            user = form.cleaned_data.get('user')
            request.session['ID'] = user.pk
            request.session['username'] = user.username
            # 操作数据库
            return redirect('用户:member')
        else:
            # 合成响应
            return render(request,'users/login.html',{'form':form})
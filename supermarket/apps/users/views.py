from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from db.base_view import VerifyLoginView
from users import set_password
from users.forms import RegisterModelForm, LoginModelForm, InfoModelForm
from users.helper import login, check_login
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

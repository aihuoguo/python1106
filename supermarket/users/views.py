
from django.shortcuts import render

# Create your views here.
from django.views import View

from users.forms import RegisterModelForm


def member(repuest):  # 个人中心
    return render(repuest,'users/member.html')

def login(repuest): # 登录
    return render(repuest,'users/login.html')

def reg(repuest): # 注册
    return render(repuest,'users/reg.html')

class RegisterView(View):

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
            pass
        else:
            return render(request,'users/reg.html',context={'form':form})
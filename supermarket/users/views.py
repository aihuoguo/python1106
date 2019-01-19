from django.shortcuts import render

# Create your views here.
def member(repuest):  # 个人中心
    return render(repuest,'users/member.html')

def login(repuest): # 登录
    return render(repuest,'users/login.html')

def reg(repuest): # 注册
    return render(repuest,'users/reg.html')


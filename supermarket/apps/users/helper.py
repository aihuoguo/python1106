from django.shortcuts import redirect

# 保存session
def login(request,user):
    request.session['ID']=user.pk
    request.session['username']=user.username
    #关闭浏览器就消失
    request.session.set_expiry(0)



# 将验证登录的方法写成装饰器
def check_login(func):
    def verify_login(request, *args, **kwargs):
        # 判断是否又session
        if request.session.get('ID') is None:
            # 跳转到登录
            return redirect('用户:login')
        else:
            # 调用原函数
            return func(request, *args, **kwargs)
    # 返回新函数
    return verify_login


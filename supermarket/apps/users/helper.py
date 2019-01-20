from django.shortcuts import redirect

# 将验证登录的方法写成装饰器
def check_login(fun):
    def verify_login(request, *args, **kwargs):
        # 判断是否登录
        if request.session.get('ID') is None:
            # 跳转到登录
            return redirect('user:登录')
        else:
            # 调用原函数
            return fun(request, *args, **kwargs)
    # 返回新函数
    return verify_login

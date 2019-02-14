from django.http import JsonResponse
from django.shortcuts import redirect

from shopping_cart.helper import json_msg


def check_bloglogin(func):
    def verify_login(request, *args, **kwargs):
        # 判断是否又session
        if request.session.get('ID') is None:
            #保存上个请求地址
            referer=request.META.get('HTTP_REFERER',None)
            if referer:
                request.session['referer']=referer
            #判断是否为ajax请求
            if request.is_ajax():
                return JsonResponse(json_msg(1,'未登录'))
            else:
                # 跳转到登录
                return redirect('用户:login')
        else:
            # 调用原函数
            return func(request, *args, **kwargs)
    # 返回新函数
    return verify_login
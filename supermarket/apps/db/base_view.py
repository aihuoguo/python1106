from django.utils.decorators import method_decorator
from django.views import View

# 用于验证需要登录后才能访问的网页
from users.helper import check_login


class VerifyLoginView(View):
    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs )
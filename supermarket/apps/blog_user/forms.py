from django import forms

from blog_user import set_password
from blog_user.models import Buser
from django_redis import get_redis_connection
#注册表单的验证
class RegformModel(forms.ModelForm):

    password = forms.CharField(max_length=20,min_length=6,
                               error_messages={"min_length":"最小长度为6",
                                               "max_length":"最大长度为20"})
    repassword = forms.CharField(max_length=20,min_length=6,
                                 error_messages={"min_length":"最小长度为6",
                                               "max_length":"最大长度为20"})
    captcha = forms.CharField(max_length=4,error_messages={"required":"不能为空！"})

    agree = forms.BooleanField(error_messages={"required":"必须勾选"})
    class Meta:
        model=Buser#验证表单USER
        fields=["tel"]#避免手机号码重复

    def clean_tel(self):#验证手机号码
        tel = self.cleaned_data.get("tel")
        flag = Buser.objects.filter(tel=tel).exists()#查看是否存在于数据库
        if flag:
            raise forms.ValidationError("手机号码已被注册")
        else:
            return tel

    def clean(self):#清洗所有数据
        pwd = self.cleaned_data.get("password")
        repwd = self.cleaned_data.get("repassword")
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({"repassword":"两次密码不一致！！"})
        try:
            captcha = self.cleaned_data.get("captcha")
            tel = self.cleaned_data.get("tel","")
            r = get_redis_connection()
            random_code = r.get(tel)
            random_code = random_code.decode("utf-8")
            if captcha and captcha != random_code:
                raise forms.ValidationError({"captcha":"验证码错误"})
        except:
            raise forms.ValidationError({"captcha": "验证码错误"})
        return self.cleaned_data



#登录表单的验证
class LoginformModel(forms.ModelForm):
    password = forms.CharField(max_length=20,min_length=6,
                               error_messages={"min_length":"最小长度为6",
                                               "max_length":"最大长度为20"})
    def clean(self):
        tel = self.cleaned_data.get("tel")
        try:
            user = Buser.objects.get(tel=tel)
            if user.status == 2:
                raise forms.ValidationError({"tel":"禁止登录"})
        except Buser.DoesNotExist:
            raise forms.ValidationError({"tel":"手机号不存在"})

        password = self.cleaned_data.get("password")
        if user.password != set_password(password):
            raise forms.ValidationError({"password":"密码错误"})
        self.cleaned_data["user"] = user
        return self.cleaned_data

    class Meta:
        model=Buser
        fields=["tel","password"]

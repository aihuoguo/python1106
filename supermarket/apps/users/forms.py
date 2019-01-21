from django import forms

from users import set_password
from users.models import Users


class RegisterModelForm(forms.ModelForm):
    # 注册表单模型类

    # 单独验证密码

    password = forms.CharField(max_length=16, min_length=8, error_messages={
        'required': '密码不能为空',
        'min_length': '密码最小长度为8位',
        'max_length': '密码最大长度为16位',
    })
    repassword = forms.CharField(max_length=16, min_length=8, error_messages={
        'required': '密码不能为空',
        'min_length': '密码最小长度为8位',
        'max_length': '密码最大长度为16位',
    })

    class Meta:
        model = Users
        fields = ['username']

        error_messages = {
            "username": {
                'required': '用户名必须填写',
                'max_length': '用户名长度不能大于20',
            }
        }

    # 判断两次密码是否一致
    def clean(self):
        pwd = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repassword')
        # 如果不一样
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({'repassword': '两次密码不一致'})
        else:
            return self.cleaned_data

    # 验证用户是否存在
    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        # 判断
        res = Users.objects.filter(username=username).exists()
        if res:
            # 如果用户名已经存在 则报错
            raise forms.ValidationError('用户已存在，请重新输入')
        else:
            # 返回用户名
            return username


# 登录表单模型类
class LoginModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=8,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码最少为8位',
                                   'max_length': '密码最多16位',

                               })

    class Meta:
        model = Users
        fields = ['username']

        error_messages = {
            'username': {
                'required': '用户名不能为空',
                'max_length': '用户名不能太长'
            }
        }

    def clean(self):
        # 验证用户名
        username = self.cleaned_data.get('username')
        # 查询数据库
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise forms.ValidationError({'username': '用户名错误'})
        # 验证密码
        password = self.cleaned_data.get('password','')
        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误'})
        # 返回清洗的数据
        self.cleaned_data['user'] = user
        return self.cleaned_data


# 个人资料表单模型类
class InfoModelForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['birth_time','school_name','address','hometown']

        error_messages = {
            "tel": {
                'required': '用户名必须填写',
                'max_length': '用户名长度不能大于10',
            }

        }


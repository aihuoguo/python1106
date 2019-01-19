from django import forms

from users.models import Users



class RegisterModelForm(forms.ModelForm):
    # 注册表单模型类

    #单独验证密码

    password = forms.CharField(max_length=16,min_length=8,error_messages={
                                                            'required':'密码不能为空',
                                                            'min_length':'密码最小长度为8位',
                                                            'max_length':'密码最大长度为16位',
                                                            })
    repassword = forms.CharField(max_length=16,min_length=8,error_messages={
                                                            'required':'密码不能为空',
                                                            'min_length':'密码最小长度为8位',
                                                            'max_length':'密码最大长度为16位',
                                                            })

    class Meta:
        model=Users
        fields=['username']

        error_messages = {
            "username": {
                'required': '用户名必须填写',
                'max_length': '用户名长度不能大于20',
            }
        }
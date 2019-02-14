from django import forms
from django.http import HttpResponse

from blog_liuyan.models import Liuyan
from blog_user.models import Buser


class CommentForm(forms.ModelForm):
    class Meta:
        model=Liuyan
        fields=['context','content_id','user_tel']
    def clean_user_tel(self):
        user_tel = self.cleaned_data.get("user_tel")
        user = Buser.objects.get(tel=user_tel)
        if user.status == 3:
            Buser.objects.filter(user_tel=user_tel).update(is_delete=1)
        if user.status != 3:
            Buser.objects.filter(user_tel=user_tel).update(is_delete=False)
            raise forms.ValidationError("禁止留言")
        else:
            return user_tel
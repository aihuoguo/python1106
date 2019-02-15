from django import forms
from django.http import HttpResponse

from blog_liuyan.models import Comment
from blog_user.models import Buser


class CommentForm(forms.ModelForm):
    # context = forms.CharField(max_length=200,min_length=1,
    #                           error_messages={"content":"最少输入一个字符"})
    class Meta:
        model=Comment
        fields=['context','content_id','user_tel']
    def clean_user_tel(self):
        user_tel = self.cleaned_data.get("user_tel")
        user = Buser.objects.get(tel=user_tel)
        if user.status == 3:
            Comment.objects.filter(user_tel=user_tel).update(is_delete=1)
        if user.status != 3:
            Comment.objects.filter(user_tel=user_tel).update(is_delete=False)
            # return HttpResponse("禁止留言")
            raise forms.ValidationError("禁止留言")
        else:
            return user_tel
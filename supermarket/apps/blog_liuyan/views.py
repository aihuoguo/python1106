from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from blog_liuyan.forms import CommentForm
from blog_liuyan.models import Liuyan


def comment(request):
    if request.method=="POST":
        data = request.POST
        form = CommentForm(data)
        if form.is_valid():
            clean_data = form.cleaned_data
            msg = Liuyan()
            msg.context = clean_data.get("context")
            msg.content_id = clean_data.get("content_id")
            msg.user_tel = clean_data.get("user_tel")
            msg.save()
            #获取上个页面的网址
            referer = request.META.get("HTTP_REFERER", None)
            if referer:
                return redirect(referer)
        else:
            return HttpResponse("禁止留言！！")


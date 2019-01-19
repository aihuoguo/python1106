from django.shortcuts import render

# Create your views here.
def index(repuest): # 首页
    return render(repuest,'commodity/index.html')


def detail(repuest): # 商品详情
    return render(repuest,'commodity/detail.html')

def category(repuest): # 超市商品列表
    return render(repuest,'commodity/category.html')
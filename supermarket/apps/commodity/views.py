from django.shortcuts import render
from django.views import View

from commodity.models import GoodsSKU, GoodsType

# 商品首页
class IndexView(View):
    def get(self, request):
        return render(request, 'commodity/index.html')

# 商品分类表
class TypeView(View):
    def get(self, request):
        #查询所有的类型
        categorys = GoodsType.objects.filter(is_delete=False)
        # 查询所有的商品
        goods_skus = GoodsSKU.objects.filter(is_delete=False)
        context={'Types':categorys,'goods_skus':goods_skus,}
        return render(request, 'commodity/category.html',context=context)

#商品详情
class DetailView(View):
    def get(self,request,id):
        # 查询数据库
        goods_sku=GoodsSKU.objects.get(pk=id)
        context={'goods_sku':goods_sku,}
        return render(request,'commodity/detail.html',context=context)
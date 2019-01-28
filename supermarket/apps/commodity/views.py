from django.shortcuts import render
from django.views import View

from commodity.models import GoodsSKU, GoodsType, Activity

# 商品首页
from shopping_cart.helper import get_cart_count


class IndexView(View):
    """商品首页"""
    def get(self,request):
        #查询数据库
        act=Activity.objects.filter(is_delete=False)
        data=GoodsSKU.objects.filter(is_delete=False)
        context={
            'act':act,
            'data':data
        }
        return render(request,'commodity/index.html',context=context)



# 商品分类表
class TypeView(View):
    def get(self, request, cate_id, order):
        # 查询所有的类型
        categorys = GoodsType.objects.filter(is_delete=False).order_by('-order')
        # 得到第一个类型
        # type=categorys.first()
        if cate_id == '':
            type = categorys.first()
            cate_id = type.pk
        else:
            # 根据类型id查询对应的类型
            cate_id = int(cate_id)
            type = GoodsType.objects.get(pk=cate_id)
        # 查询某个类型下的所有商品
        goods_skus = GoodsSKU.objects.filter(is_delete=False, goods_type=type)
        # print(goods_skus)
        # 判断order的值
        if order == '':
            order = 0
        order = int(order)
        # print(order)
        # 排序规则
        order_rule = ['pk', '-sales_val', 'price', '-price', '-create_time']
        # print(order_rule)
        goods_skus = goods_skus.order_by(order_rule[order])

        #获取当前用户 购物车的总数量
        cart_count=get_cart_count(request)

        context = {'categorys': categorys,
                   'goods_skus': goods_skus,
                   'cate_id': cate_id,
                   'order': order,
                   'cart_count':cart_count}

        return render(request, 'commodity/category.html', context=context)


# 商品详情
class DetailView(View):
    def get(self, request, id):
        # 查询数据库
        goods_sku = GoodsSKU.objects.get(pk=id)
        context = {'goods_sku': goods_sku, }
        return render(request, 'commodity/detail.html', context=context)

# 首页活动轮播图






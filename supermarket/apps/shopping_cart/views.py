from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# def shopcart(repuest):  # 购物车
#     return render(repuest,'shopping_cart/shopcart.html')
from django.views import View
from django_redis import get_redis_connection

from commodity.models import GoodsSKU
from db.base_view import VerifyLoginView

from shopping_cart.helper import json_msg, get_cart_count, get_cart_key


# 添加购物车数据
class AddCartView(VerifyLoginView):
    def post(self, request):
        # 接受参数
        user_id = request.session.get('ID')
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 判断是否为整数
        try:
            sku_id = int(sku_id)
            count = int(count)
        except:
            return JsonResponse(json_msg(1, '参数错误'))
        # 要在数据库中存在商品
        try:
            goods_sku = GoodsSKU.objects.get(pk=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse(json_msg(2, '商品不存在'))

        # 判断库存
        if goods_sku.stock < count:
            return JsonResponse(json_msg(3, '库存不足'))

        # 操作数据
        # 连接redis
        # 创建连接
        r = get_redis_connection()
        # 处理购物车的key
        cart_key = f'cart_{user_id}'

        # 添加
        # 获取购物车中已经存在的数量加上需要添加 的 与库存比较
        old_count = r.hget(cart_key, sku_id)  # 得到的时二进制数据
        if old_count is None:
            old_count = 0
        else:
            old_count = int(old_count)
        if goods_sku.stock < old_count + count:
            return JsonResponse(3, '库存不足')

        # 将商品添加到购物车
        r.hincrby(cart_key, sku_id, count)

        # 获取购物车中的总数量
        cart_count = get_cart_count(request)
        print(cart_count)

        # 合成响应
        return JsonResponse(json_msg(0, '添加购物车成功', data=cart_count))


# 购物车列表
class CartListView(View):
    def get(self, request):
        # 从session获取用户的id
        user_id = request.session.get("ID")
        # 连接redis
        r = get_redis_connection()
        # 准备键
        cart_key = get_cart_key(user_id)
        # 从redis获取购物车全部的商品信息
        cart_datas = r.hgetall(cart_key)
        # 准备一个空列表,保存多个商品
        goods_skus = []
        # 遍历字典
        for sku_id, count in cart_datas.items():
            # 遍历得到的数据为二进制数据，需强行转化
            sku_id = int(sku_id)
            count = int(count)
            # 根据购物车里的商品id查询出所有商品信息
            try:
                goods_sku = GoodsSKU.objects.get(pk=sku_id, is_delete=False, is_on_sale=True)
            except GoodsSKU.DoesNotExist:
                # 删除redis过期数据
                r.hdel(cart_key,sku_id)
                continue
            # 将购物车中数量和商品信息合成一块儿(给一个已经存在的对象添加属性)
            goods_sku.count = count
            # 保存商品到商品列表
            goods_skus.append(goods_sku)
            # print(goods_skus)
        # 渲染数据
        context = {
            'goods_skus': goods_skus
        }
        return render(request, 'shopping_cart/shopcart.html', context=context)

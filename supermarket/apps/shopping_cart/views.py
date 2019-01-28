from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# def shopcart(repuest):  # 购物车
#     return render(repuest,'shopping_cart/shopcart.html')
from django.views import View
from django_redis import get_redis_connection

from commodity.models import GoodsSKU
from db.base_view import VerifyLoginView


from shopping_cart.helper import json_msg, get_cart_count

# 添加购物车数据
class AddCartView(VerifyLoginView):
    def post(self,request):
        # 接受参数
        user_id=request.session.get('ID')
        sku_id=request.POST.get('sku_id')
        count=request.POST.get('count')

        # 判断是否为整数
        try:
            sku_id=int(sku_id)
            count=int(count)
        except:
            return JsonResponse(json_msg(1,'参数错误'))
        # 要在数据库中存在商品
        try:
            goods_sku=GoodsSKU.objects.get(pk=sku_id)
        except GoodsSKU.DoesNotExist:
            return  JsonResponse(json_msg(2,'商品不存在'))

        # 判断库存
        if goods_sku.stock<count:
            return JsonResponse(json_msg(3,'库存不足'))

        # 操作数据
        #连接redis
        #创建连接
        r=get_redis_connection()
        # 处理购物车的key
        cart_key=f'cart_{user_id}'

        #添加
        #获取购物车中已经存在的数量加上需要添加 的 与库存比较
        old_count= r.hget(cart_key,sku_id) # 得到的时二进制数据
        if old_count is None:
            old_count=0
        else:
            old_count=int(old_count)
        if goods_sku.stock<old_count+count:
            return  JsonResponse(3,'库存不足')

        # 将商品添加到购物车
        r.hincrby(cart_key,sku_id,count)

        #获取购物车中的总数量
        cart_count=get_cart_count(request)
        print(cart_count)

        # 合成响应
        return JsonResponse(json_msg(0,'添加购物车成功',data=cart_count))


# 减少购物车数据
class DelCartView(VerifyLoginView):
    def post(self,request):
        # 接受参数
        user_id=request.session.get('ID')
        sku_id=request.POST.get('sku_id')
        count=request.POST.get('count')

        # 判断是否为整数
        try:
            sku_id=int(sku_id)
            count=int(count)
        except:
            return JsonResponse(json_msg(1,'参数错误'))
        # 要在数据库中存在商品
        try:
            goods_sku=GoodsSKU.objects.get(pk=sku_id)
        except GoodsSKU.DoesNotExist:
            return  JsonResponse(json_msg(2,'商品不存在'))

        # 判断库存
        if goods_sku.stock<count:
            return JsonResponse(json_msg(3,'库存不足'))

        # 操作数据
        #连接redis
        #创建连接
        r=get_redis_connection()
        # 处理购物车的key
        cart_key=f'cart_{user_id}'

        #添加
        #获取购物车中已经存在的数量加上需要添加 的 与库存比较
        old_count= r.hget(cart_key,sku_id) # 得到的时二进制数据
        if old_count is None:
            old_count=0
        else:
            old_count=int(old_count)
        if goods_sku.stock<old_count+count:
            return  JsonResponse(3,'库存不足')

        # 将商品添加到购物车
        r.hincrby(cart_key,sku_id,count)

        #获取购物车中的总数量
        cart_count=get_cart_count(request)
        print(cart_count)

        # 合成响应
        return JsonResponse(json_msg(0,'减少购物车成功',data=cart_count))

# 购物车
class CartView(View):
    def get(self,request):
        return render(request,'shopping_cart/shopcart.html')
from django.shortcuts import render

# Create your views here.

def shopcart(repuest):  # 购物车
    return render(repuest,'shopping_cart/shopcart.html')
from django.shortcuts import render

# Create your views here.
def allorder(repuest): # 全部订单
    return render(repuest,'order/allorder.html')

def order(repuest): # 确认订单
    return render(repuest,'order/order.html')

def orderdetail(repuest): # 订单详情
    return render(repuest,'order/orderdetail.html')

def pay(repuest): # 完成支付
    return render(repuest,'order/pay.html')

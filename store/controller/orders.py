from django.shortcuts import render,redirect
from django.contrib import messages
# from .forms import customForm
from django.http import JsonResponse
from store.models import Product,Cart,Wishlist,Order,OrderItem,Profile
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
from django.http import HttpResponse



@login_required(login_url='loginpage')
def index(request):
    orders = Order.objects.filter(user = request.user)
    return render(request,'store/orders/myorders.html',{'orders':orders})



@login_required(login_url='loginpage')
def vieworder(request,t_no):
    order = Order.objects.filter(tracking_no = t_no).filter(user = request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context ={
        'orders':order,
        'orderitems':orderitems
    }
    return render(request,'store/orders/o_view.html',context)

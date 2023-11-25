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
def checkout(request):
    rawcart = Cart.objects.filter(user = request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty
    
    userprofile = Profile.objects.filter(user = request.user).first()

    context = {'caritems':cartitems,'total_price':total_price,'userprofile':userprofile}
    return render(request,'store/checkout.html',context)


@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':
        currentuser = User.objects.filter(id = request.user.id).first()
        if  not currentuser.first_name:
            currentuser.first_name = request.POST.get("fname")
            currentuser.last_name = request.POST.get("lname")
            currentuser.save()
        if not Profile.objects.filter(user = request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.Phone = request.POST.get('mobile')
            userprofile.address = request.POST.get('address')
            userprofile.country = request.POST.get('country')
            userprofile.state = request.POST.get('state')
            userprofile.city = request.POST.get('city')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.Phone = request.POST.get('mobile')
        neworder.address = request.POST.get('address') 
        neworder.country = request.POST.get('country')
        neworder.state = request.POST.get('state')
        neworder.city = request.POST.get('city')
        neworder.pincode = request.POST.get('pincode')
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_Id = request.POST.get('payment_id')





        cart = Cart.objects.filter(user = request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        neworder.total_price = cart_total_price
        trackno = 'mahesh' + str(random.randint(111111111,999999999))
        while Order.objects.filter(tracking_no = trackno) is None:
            trackno = 'mahesh' + str(random.randint(11111,99999))

        neworder.tracking_no = trackno
        neworder.save()
            
        neworderitems = Cart.objects.filter(user = request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order =neworder,
                product =item.product,
                price = item.product.selling_price,
                quantity = item.product_qty
            )
            orderproduct = Product.objects.filter(id=item.product.id).first()
            orderproduct.quantity -= item.product_qty
            orderproduct.save()

        Cart.objects.filter(user = request.user).delete()

        messages.success(request,"Your Order Placed successfully..")
        paymode = request.POST.get('payment_mode')
        if paymode == 'paid with rajorpay':
            return JsonResponse({'status':"Your Order Placed successfully.."})

    return redirect('/home')
 
@login_required(login_url='loginpage')
def RozarpayCheck(request):
    cart = Cart.objects.filter(user = request.user)
    total_price =0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty
    return JsonResponse({"total_price":total_price})

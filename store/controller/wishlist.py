from django.shortcuts import render,redirect
from django.contrib import messages
# from .forms import customForm
from django.http import JsonResponse
from store.models import Product,Cart,Wishlist
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def wishlist(request):
    wishlistitems = Wishlist.objects.filter(user = request.user)
    context ={
        'wishlist':wishlistitems
    }
    return render(request,'store/wish.html',context)


def addtowish(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id = prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user = request.user,product_id = prod_id)):
                    return JsonResponse({'status':'Product is all ready exist'})
                else:
                    Wishlist.objects.create(user = request.user,product_id = prod_id)
                    return JsonResponse({'status':'Add to wish list Successfully ..'})
            else:
                return JsonResponse({'status':'No such Product Found '})
        else:
            return JsonResponse({'status':'Login to Continue..'})
    return redirect('/home')


def deletetowish(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Wishlist.objects.filter(user = request.user,product_id = prod_id)):
            wishitem = Wishlist.objects.get(product_id = prod_id,user = request.user)
            wishitem.delete()
            return JsonResponse({'status':'Deletd Successfully..'})
    return redirect('/home')
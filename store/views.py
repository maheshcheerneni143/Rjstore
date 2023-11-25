from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse

from .models import *
# Create your views here.

def store(request):
    trending_items = Product.objects.filter(trending=1)
    context = {
        'trend':trending_items
    }
    return render(request,'store/index.html',context)



def collection(request):
    collections= Category.objects.filter(status=0)
    context = {
        'collections':collections,
    }
    return render(request,'store/collections.html',context)

def collectionview(request,slug):
    if(Category.objects.filter(slug = slug,status = 0)):
        product = Product.objects.filter(category__slug = slug)
        category_name = Category.objects.filter(slug=slug).first()
        context ={
            'product':product,'category_name':category_name
        }

        return render(request,'store/product/p_index.html',context)
    else:
        messages.warning(request,'No such items not found')
        return redirect('collections')

def productview(request,cat_slug,prod_slug):
    if(Category.objects.filter(slug=cat_slug,status = 0)):
        if(Product.objects.filter(slug=prod_slug,status = 0)):
            products=Product.objects.filter(slug=prod_slug,status = 0).first()
            context ={
                'products':products,
            }
        else:
            messages.error(request,'No such product is found')
            return redirect('collections')
    else:
        messages.error(request,'No such product is found')
        return redirect('collections')

    return render(request,'store/product/p_view.html',context)


def productlistajax(request):
    products = Product.objects.filter(status=0).values_list('name',flat =True)
    product_list = list(products)
    return JsonResponse(product_list, safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searchname = request.POST.get('searchproductname')
        if searchname == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=Product.objects.filter(name__contains=searchname).first()
            if product:
                return redirect('collections/' + product.category.slug +'/' +product.slug)
            else:
                messages.info(request,'No such products found')
                return redirect(request.META.get('HTTP_REFERER'))


    return redirect(request.META.get('HTTP_REFERER'))
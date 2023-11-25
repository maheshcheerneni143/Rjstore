from django.shortcuts import render,redirect
from django.contrib import messages
# from .forms import customForm
from store.forms import customForm
from store.models import User
from django.contrib.auth import authenticate,login,logout




def register(request):
    form = customForm
    if request.method == 'POST':
        form = customForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully  ! login to continue..')
            return redirect('/login')
    return render(request,'store/auth/register.html',{'form':form})



def Login(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are allready Logged In..')
        return redirect('/home/')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passw = request.POST.get('password')
            user = authenticate(username = name , password = passw)
            if user is not None:
                login(request,user)
                messages.success(request,'You are Logged In Successfully..')
                return redirect('/home/')
            else:
                messages.error(request,'You are Entered Invalid useraname and password')
                return redirect('/login')
        return render(request,'store/auth/login.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'You are Logged Out Successfully..')
    return redirect('/home/')

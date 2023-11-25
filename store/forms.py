from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User




class customForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','palceholder':"Enter user name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','palceholder':"Enter Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','palceholder':"Enter a Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','palceholder':"Enter a Password"}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



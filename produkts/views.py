from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
# Create your views here.

def products_page(request):
    products = Product.objects.all() # SELECT * FROM PRODUCTS
    return  render(request,'products/products.html',{"products":products})

def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return  render(request, 'products/order.html',{'form':form})



def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'products/register.html', {'form':form})
def userlist(request):
    user = User.objects.all()
    return render(request, 'products/user.html', {"user": user})

def aboutUs_page(request):
    about_us = AboutUs.objects.all()
    return render(request, 'products/AboutUs.html',{'about_us': about_us})
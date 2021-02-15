import token

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from .filters import ProductFilter
from store.settings import EMAIL_HOST_USER
from .models import *
from .forms import OrderForm,ProfileForm
# Create your views here.
from .templates.products.tokens import account_activation_token

# Create your views here.

def products_page(request):
    products = Product.objects.all() # SELECT * FROM PRODUCTS
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    return render(request, 'products/products.html', {"products": products, 'filter':filter})
def order_page(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        total_price = 0
        form = OrderForm(initial={'product': product})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                total_price = product.price * form.cleaned_data['quantity']
        return render(request, 'products/order.html', {'form': form, 'total_price': total_price})
    except Product.DoesNotExist:
        return HttpResponse('Not Found')



def register_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            subject = "welcome to our  site!!!"
            body = "Activate your account!"
            from_email = EMAIL_HOST_USER
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            message = EmailMessage(subject=subject, body=body, from_email=from_email, to=[to_email,])
            message.send()
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('products')
    return render(request, 'products/register.html', {'form': form})

def userlist(request):
    user = User.objects.all()
    return render(request, 'products/user.html', {"user": user})

def aboutUs_page(request):
    about_us = AboutUs.objects.all()
    return render(request, 'products/AboutUs.html',{'about_us': about_us})

def logout_page(request):
    logout(request)
    return redirect('/')



def accound_settings(request):
    user = request.user.profile
    order_user = request.user
    orders = order_user.order_set.all()
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context = {'form': form,'orders':orders}
    return  render(request,'products/profile.html',context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

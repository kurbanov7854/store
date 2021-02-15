from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class OrderForm(forms.ModelForm):
    class  Meta:
        model = Order
        fields = ['product','quantity']

class ProfileForm(forms.ModelForm):

    class Meta:
        model =  Profile
        fields = '__all__'

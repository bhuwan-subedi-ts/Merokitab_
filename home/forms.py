from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from home.models import Product, Review

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','photo','details','category','price','featured','ISBN','author','publication','abstract']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from home.models import Product,Contact
from home.forms import CreateUserForm,AddProductForm,ReviewForm
from django.contrib import messages

# Create your views here.

def home(request): 
    query = Product.objects.all()
    qu = Product.objects.values_list('category',flat=True)
    context = {'query':query,'qu':qu}
    
    return render(request,'homepage.html',context)

def addproduct(request):
    form = AddProductForm()
    if request.user.is_authenticated:
        #prod = request.user
        if request.method == "POST":

            form = AddProductForm(request.POST,request.FILES)
            
            if form.is_valid:
                user = form.save(commit=False)
                print(user)
                user.posted_by = request.user
                user.save()

        return render(request,'add_product.html',{'form': form})
             
    else:
        return redirect('/login')


def login_view(request):
    query = Product.objects.all()
    context = {'query':query}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,'homepage.html',context)
    
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def userprofile(request):
    return render(request,'userprofile.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        res = Product.objects.filter(name__contains=searched)
        return render(request,'search.html',{'searched':searched,'res':res})
    
    return render(request,'search.html')

def signup_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return render(request,'login.html')

    context = {'form':form}
    return render(request,'signup.html',context)
def prod_detail(request,pk):
    produc = Product.objects.get(id=pk)
    rev = produc.comments.all()
    comment_form = ReviewForm(data=request.POST)
    new_comment=None
    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.product = produc
            new_comment.user = request.user
            new_comment.save()
    context = { 'produc':produc,'comment_form':comment_form,'rev':rev,'new_comment':new_comment }
    return render(request,'prod_details.html',context)

        
def contactus(request):
    if request.method=="POST":
        #storing the data obtained from contact me page in variables.        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #creating an instance and saving the data to database
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    
    return render(request,'contact.html')
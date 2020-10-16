from django.db import models
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from home.models import Product,Contact
from home.forms import CreateUserForm,AddProductForm
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
    #if request.method == 'POST':
        #storing the data obtained from contact me page in variables.
        #name = request.POST['name']
        #state = request.POST['state']
        #district = request.POST['district']
        #town = request.POST['town']
        #ward = request.POST['ward']
        #prof = request.POST['prof']
        #nterest = request.POST['interest']
        #email = request.POST['email']
        #phone = request.POST['phone']
        #password = request.POST['password']
        #cnfpassword = request.POST['cnfpassword']
       #store image file here
        #creating an instance and saving the data to database
        #if password == cnfpassword:  
        #    user = User(name=name,add_state=state,add_district=district,add_town=town,add_ward=ward,prof=prof,interest=interest,email=email,phone_number=phone,password=password)
        #    user.save()
        #    print("data Saved!")
        #    return render(request,'login.html')
        #else:
        #    print("password doesn't match")

    #return render(request,'signup.html')
    
    
    

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
        #print("the data saved successfully!")
        
        #sender_name = name
        #sender_email = email
        #descAndnum = desc + " : " + "Phone Number = "+phone + " Email = "+email

        #message = "{0} has sent you a new message:\n\n{1}".format(sender_name, descAndnum)
        
        #send_mail('New Enquiry In Portfolio', message, sender_email, ['ghimirebibek75235@gmail.com'], fail_silently= False)
    
    return render(request,'contact.html')
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def home_page(request):
    user = request.user
    return render(request,'home.html',{'name':user})

def signup_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        # print(username,email)
        if not username.isalnum():
            msg=messages.error(request, 'Username must contain only alphanumeric characters.')
            return redirect('signup')
        my_user=User.objects.create_user(username,email,pass1)
        my_user.save()
        return redirect('login')
    
    
    
    return render(request,'signup.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        print(username,pass1)
        
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("plz check pass and username")
        
    return render(request,'login.html')



def logout_page(request):
    logout(request)
    return redirect('login')

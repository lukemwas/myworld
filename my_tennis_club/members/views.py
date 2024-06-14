from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login') 
def homepage(request):
    return render(request, 'home.html', )

def loginpage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('uer user name or password is not correct')


    return render(request,'login.html',)

def signuppage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('CHECK YOUR PASSWORDS AGAIN')
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            #return HttpResponse('user has been created')
        return redirect('login')
        #print(uname,email,pass1,pass2)

    return render(request,'signup.html',)

def logoutpage(request):
    logout(request)
    return redirect('login')
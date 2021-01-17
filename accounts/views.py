from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')



# we aare using same register() to fetch register.html and during submission of registration form.
# this is possible only via GET (-> used in fetching register.html) and POST (-> used in form method) methods
def register (request):
    if request.method=='POST':  
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        # mobile_no=request.POST['mobile_no']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken already...')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email id registered earlier...')
                return redirect('register')
            else: 
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Oops, Password does not match...')
            return redirect('register') 
        return redirect('/')

    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')
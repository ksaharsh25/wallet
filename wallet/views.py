from django.shortcuts import render,redirect
from .models import *
import random 
# Create your views here.

def register(request):
    if request.method== 'POST':
        email=request.POST['email']
        mobile=request.POST['mobile']
        name=request.POST['name']
        
        # print(password)
        payment=Register(email=email,mobile=mobile,name=name)
        payment.save()     
        return redirect('login')
    return render(request,'signup.html')


def get_otp():
    otp = ""
    for i in range(4):
        otp += str(random.randint(1,9))
    return otp


def login(request):
    if request.method=="POST":
        mobile=request.POST.get('mobile')
        
        try:
            mob=Login.objects.get(mobile=mobile)

            

        except:
            Login.objects.create(mobile=mobile)
            mob=Login.objects.get(mobile=mobile)

        OTP=get_otp()
        mob.otp=OTP
        mob.save()
        request.session['mobile']=mobile
        return redirect('verify')    
    return render(request,'login.html')


def verify(request):
    mobile=request.session['mobile']
    context={'mobile':mobile}

    if request.method=="POST":
        otp=request.POST.get('otp')
        verify=Login.objects.get(mobile=mobile)

        if verify.otp == int(otp):
            Login.objects.filter(mobile=mobile)
            print("Verified")
            return redirect('register')
        else:
            print("Wrong OTP!")
    return render(request,"verify.html",context)        


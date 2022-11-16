from django.shortcuts import render,redirect,HttpResponse
from .models import *
import random 

# Create your views here.
# from django.template import loader
from django.views.decorators.csrf import csrf_protect
# def register(request):
#     if request.method== 'POST':
#         email=request.POST['email']
#         mobile=request.POST['mobile']
#         name=request.POST['name']
        
#         # print(password)
#         payment=Register(email=email,mobile=mobile,name=name)
#         payment.save()     
#         return redirect('login')
#     return render(request,'signup.html')
def register(request):
    if request.method=="POST":
        name=request.POST['name']
        mobile=request.POST['mobile']
        
        admi=Person(name=name,mobile=mobile)
        admi.save()
        return redirect('login')
    return render(request, 'signup.html',)

def get_otp():
    otp = ""
    for i in range(4):
        otp += str(random.randint(1,9))
    return otp


def login(request):
    if request.method=="POST":
        mobile=request.POST.get('mobile')
        
        try:
            mob=Person.objects.get(mobile=mobile)

        except:
            Person.objects.create(mobile=mobile)
            mob=Person.objects.get(mobile=mobile)

        OTP=get_otp()
        mob.otp=OTP
        mob.save()
        request.session['mobile']=mobile
        return redirect('verify')    
    return render(request,'login.html')


def verify(request):
    Add=Person.objects.all()
   
    mobile=request.session['mobile']
    # context={'mobile':mobile}
    
    if request.method=="POST":
        otp=request.POST.get('otp')
        verify=Person.objects.get(mobile=mobile)

        if verify.otp == int(otp):
            Person.objects.filter(mobile=mobile)
            
         
            return redirect("wallet",mobile)
        else:
            print("Wrong OTP!")
    return render(request,"verify.html",{"add":Add})        

def Wallet(request,mobile):
    data = Person.objects.filter(mobile=mobile).first()
    request.session['mobile']=mobile 
    

    return render(request,"wallet.html",{"Data":data})
    
# @csrf_protect
def add(request,mobile):
    request.session['mobile']=mobile 
    Add=Person.objects.get(mobile=mobile) 
    
    #     account_number=request.POST['account_number']
    #     add_money=request.POST['add_money']

    #     gift=wallet(account_number=account_number,add_money=add_money)
    #     gift.save()

          
            
    ID={"add":Add}   
    return render(request,"add.html",ID) 

def withdraw(request,mobile):
    base=request.session['mobile']=mobile
    id={"base":base}
    return render(request,"withdraw.html",{"id":id})

# def edit(request,pk):
#     user=User.objects.get(Id=pk)
#     form=EmployeeForm(instance=user) 
#     if request.method=='POST':
#         form=EmployeeForm(request.POST,instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#     context = {
#         'user': user,
#         'form': form,
#     }        
#     return render(request,"edit.html",context)    




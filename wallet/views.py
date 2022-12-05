from django.shortcuts import render,redirect,HttpResponse
from wallet.models import *
import random 

def register(request):
    
    if request.method=="POST":
        try:
            
            name=request.POST['name']
            mobile=request.POST['mobile']
            
            admi=Person(name=name,mobile=mobile)
            
            admi.save()
            
        except admi.DoesNotExist:
            print("Error!")
        return redirect('login')    
        
    return render(request, 'signup.html')

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
            
        request.session['mobile']=mobile
        OTP=get_otp()
        mob.otp=OTP
        mob.save()
        
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
    # data2=wallet.objects.get(use=use)
    request.session['mobile']=mobile
     
    
    return render(request,"wallet.html",{"Data":data})
    

def add(request,mobile):
    if request.session['mobile']==mobile:
   
    
        if request.method=="POST":
            Balance=request.POST['Balance']
            user=Person.objects.get(mobile=mobile)
            amount=int(user.Balance)
            amount+=int(Balance)
            user.Balance=str(amount)
            user.save()
            return redirect("wallet",mobile)
    return render(request,"add.html")

       

def withdraw(request,mobile):

    request.session['mobile']=mobile
    if request.method=="POST":
         Balance=request.POST['Balance']
         user=Person.objects.get(mobile=mobile)
         amount=int(user.Balance)
         amount-=int(Balance)
         user.Balance=str(amount)
         user.save()
         return redirect("wallet",mobile) 
    return render(request,"withdraw.html")



def bank_transfer(request):
    
    if request.method=="POST":
        account_number=request.POST['account_number']
        send_money=request.POST['send_money']
        bank=wallet(account_number=account_number,send_money=send_money)
        sent=int(bank.send_money)
        sent += int(send_money)
        bank.send_money=str(sent)
        bank.save()
        return redirect('transaction_done')
            
    
    return render(request,"banktransfer.html")

def transaction_done(request):
         
    return render(request,"transaction_done.html")
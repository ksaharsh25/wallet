from django.shortcuts import render,redirect,HttpResponse
from wallet.models import *
import random 
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.contrib.auth.decorators import login_required

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
        ban=bank(account_number=account_number,send_money=send_money)
        sent=int(ban.send_money)
        sent += int(send_money)
        ban.send_money=str(sent)
        ban.save()
        return redirect('transaction_done',account_number)
            
    
    return render(request,"banktransfer.html")

def transaction_done(request,account_number):
    request.session['account_number']=account_number
    transfer=bank.objects.filter(account_number=account_number).first()
    detail={'transfer':transfer}
         
    return render(request,"transaction_done.html",detail)
@login_required
def inbox(request):
    user=request.user
    messages=Message.get_messages(user=user)  
    active_direct=None
    directs=None

    if messages:
        message=messages[0]
        active_direct=message['user'].username
        directs=Message.objects.filter(user=user,recipient=message['user'])
        directs.update(is_read=True)
        for message in messages:
            if message['user'].username == "active_direct":
                message['unread']=0
        context={
            'directs':directs,
            'messages':messages,
            'active_direct':active_direct,
            } 
    # template= loader.get_template             
def marks(request,mobile):
    request.session['mobile']=mobile
    mark=Person.objects.get(mobile=mobile)
    if request.method=="POST":
        
        mark.marks=int(mark.physics)+int(mark.chemistry)+int(mark.maths)+int(mark.english)
        mark.save()
    
    return render(request,"marks.html",{"mark":mark})

def points1(request,mobile):
    request.session['mobile']==mobile
    point1=Person.objects.get(mobile=mobile)
    if int(100)<=point1.marks<int(200):
    
        point1.marks= int(point1.marks)-int(100)
        point1.save()
    else:
        print("Error")
    return render(request,"points1.html",{"point1":point1})   

def points2(request,mobile):
    
    point2=Person.objects.get(mobile=mobile)
    if point2.marks>=int(200):
       point2.marks= int(point2.marks)-int(200)
    return render(request,"points2.html",{"point2":point2})      
from django.shortcuts import render,redirect
from .models import *
import random 
# Create your views here.
from .forms import *
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
    # context={'mobile':mobile}

    if request.method=="POST":
        otp=request.POST.get('otp')
        verify=Login.objects.get(mobile=mobile)

        if verify.otp == int(otp):
            Login.objects.filter(mobile=mobile)
            print("Verified")
            return redirect('wallet')
        else:
            print("Wrong OTP!")
    return render(request,"verify.html")        

def list(request):
    List=balance.objects.all()
    
    return render(request,"list.html",{'list':List})

def wallet(request):
    Add=balance.objects.all()
    # if request.method=="POST":
    #     Balance=request.POST['Balance']
    #     amount=request.POST['amount']
    #     add_money=Balance+int(amount)
    #     withdraw=Balance-int(amount)
    #     user=balance.objects.filter(add_money=add_money,withdraw=withdraw)
    #     user.save()
    return render(request,"wallet.html",{"add":Add})

def add(request):
    if request.method=='POST':
        account=request.POST['account']
        amount=request.POST['amount']

        add=balance(account=account,amount=amount)
        add.save()
    return render(request,"add.html")



def edit(request,pk):
    user=balance.objects.get(id=pk)
    form=EmployeeForm(instance=user) 
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'user': user,
        'form': form,
    }        
    return render(request,"edit.html",context)    
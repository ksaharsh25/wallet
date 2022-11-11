from django.shortcuts import render,redirect
from .models import *
import random 
# Create your views here.
from .forms import *
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
    # Add=Login.objects.get(id=pk)
    # ID={"add":Add}
    mobile=request.session['mobile']
    # context={'mobile':mobile}

    if request.method=="POST":
        otp=request.POST.get('otp')
        verify=Login.objects.get(mobile=mobile)

        if verify.otp == int(otp):
            Login.objects.filter(mobile=mobile)
            pk = Login.objects.get('pk')
            Add=Login.objects.get(id=pk)
            ID={"add":Add}
            print("Verified")
            return redirect('/wallet/<str:pk>')
        else:
            print("Wrong OTP!")
    return render(request,"verify.html",ID)        

def list(request):
    List=Login.objects.all()
    
    return render(request,"list.html",{'list':List})

def wallet(request,pk):
    Add=Login.objects.get(id=pk)
    ID={"add":Add}
   
        
    return render(request,"wallet.html",ID)

def add(request,pk):
    Add=Login.objects.get(id=pk)
    ID={"add":Add}
    if request.method=='POST':
        account=request.POST['account']
        amount=request.POST['amount']

        add=Login(account=account,amount=amount)
        add.save()
    return render(request,"add.html",ID) 


def create(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
def edit(request,pk):
    user=Login.objects.get(id=pk)
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
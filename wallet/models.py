from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw    
from django.db.models import Max

class Person(models.Model):
    mobile=models.IntegerField(max_length=100,null=True)
    otp=models.IntegerField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True)
    name=models.CharField(max_length=100,blank=True)
    Balance=models.IntegerField(blank=True,null=True,default="0") 
    Bank_name=models.IntegerField(max_length=50,blank=True,null=True)
    IFSC_Code=models.CharField(max_length=100,blank=True)
    qr_code=models.ImageField(upload_to='images',blank=True)
    image=models.ImageField(upload_to="images",blank=True)
    physics=models.IntegerField(max_length=50,blank=True,null=True,default="0")
    chemistry=models.IntegerField(max_length=50,blank=True,null=True,default="0")
    maths=models.IntegerField(max_length=50,blank=True,null=True,default="0")
    english=models.IntegerField(max_length=50,blank=True,null=True,default="0")
    marks=models.IntegerField(max_length=5,blank=True,null=True,default="0")
    # transaction_id=models.IntegerField(max_length=50,blank=True)
    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.name)
        canvas=Image.new('RGB',(290,290),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.name}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)   

class wallet(models.Model):
    use=models.OneToOneField(Person,on_delete=models.CASCADE,null=True,blank=True)
   
    
    def _str_(self):
        return str(self.use) 

    def mobile(self):
        return self.use.mobile

    def name(self):
        return self.use.name
        
                 

class bank(models.Model):
     
    account_number= models.IntegerField(max_length=100,blank=True,null=True)
    send_money=models.IntegerField(max_length=100,blank=True,null=True,default="0")

    


def create_wallet(sender,instance,created,**kwargs):
    if created:
        Person.objects.create(mobile=instance) 
        instance.save() 
post_save.connect(create_wallet,sender=wallet)


class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    recipient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    body=models.TextField(max_length=500,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

    def send_message(from_user,to_user,body):
        sender_message=Message(
            user=from_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True)
        sender_message.save()

        recipient_message=Message(
            user=to_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True)
        recipient_message.save()   

    def get_messages(user):
        users=[]
        messages=Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last') 
        for message in messages:
            users.append({
                'user':User.objects.get(pk=message['recipient']),
                'last':message['last'],
                'unread':Message.objects.filter(user=user,recipient__pk=message['recipient'],is_read=False)
            }) 
        return users
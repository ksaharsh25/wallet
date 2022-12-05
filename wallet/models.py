from django.db import models
from django.db.models.signals import post_save
# Create your models here.
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw    

class Person(models.Model):
    mobile=models.IntegerField(max_length=100,null=True,unique=True)
    otp=models.IntegerField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    Balance=models.IntegerField(blank=True,null=True,default="0") 
    Bank_name=models.IntegerField(max_length=50,blank=True,null=True)
    IFSC_Code=models.CharField(max_length=100,blank=True)
    qr_code=models.ImageField(upload_to='images',blank=True)
    # transaction_id=models.IntegerField(max_length=50,blank=True)
    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.name)
        canvas=Image.new('RGB',(250,250),'white')
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
    account_number= models.IntegerField(max_length=100,blank=True,null=True)
    
    send_money=models.IntegerField(max_length=100,blank=True,null=True)
    
    def _str_(self):
        return str(self.use) 

    def mobile(self):
        return self.use.mobile

    def name(self):
        return self.use.name         

class bank(models.Model):
    Transaction_ID=models.OneToOneField(wallet,on_delete=models.CASCADE,null=True)    

def create_wallet(sender,instance,created,**kwargs):
    if created:
        Person.objects.create(mobile=instance) 
        instance.save() 
post_save.connect(create_wallet,sender=wallet)
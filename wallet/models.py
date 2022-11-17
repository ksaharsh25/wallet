from django.db import models
from django.db.models.signals import post_save
# Create your models here.

    

class Person(models.Model):
    mobile=models.IntegerField(max_length=100,editable=False,null=True)
    otp=models.IntegerField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True)
    name=models.CharField(max_length=100,blank=True)
    
    Bank_name=models.IntegerField(max_length=50,blank=True,null=True)
    IFSC_Code=models.CharField(max_length=100,blank=True)
    
    
class wallet(models.Model):
    use=models.OneToOneField(Person,on_delete=models.CASCADE,unique=True,editable=False,null=True)
    account_number= models.IntegerField(max_length=100,blank=True,null=True)
    Balance=models.IntegerField(blank=True,null=True) 
    add_money= models.IntegerField(max_length=100,null=True,blank=True)
    withdraw=models.IntegerField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.use) 

    def mobile(self):
        return self.use.mobile

    def name(self):
        return self.use.name         

def create_wallet(sender,instance,created,**kwargs):
    if created:
        wallet.objects.create(use=instance) 
        instance.save()
post_save.connect(create_wallet,sender=Person)               
from django.db import models

# Create your models here.

    

class Login(models.Model):
    mobile=models.IntegerField(max_length=100,null=True)
    otp=models.IntegerField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True)
    name=models.CharField(max_length=100,blank=True)
    Balance=models.IntegerField(blank=True,null=True)
    amount= models.IntegerField(max_length=100,null=True)
    withdraw=models.IntegerField(max_length=100,null=True) 
    account= models.IntegerField(max_length=100,null=True)
    add_money= models.IntegerField(max_length=100,null=True)
    withdraw  = models.IntegerField(max_length=100,null=True)
    id = models.IntegerField(primary_key=True )
    
    
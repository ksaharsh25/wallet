from django.db import models
import uuid
# Create your models here.
class Register(models.Model):
    mobile=models.IntegerField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,blank=True)
    name=models.CharField(max_length=100,blank=True)

class Login(models.Model):
    mobile=models.IntegerField(max_length=100,null=True)
    otp=models.IntegerField(max_length=100,blank=True,null=True)

class balance(models.Model):
    admin=models.ForeignKey('Register',on_delete=models.CASCADE)
    Balance=models.IntegerField(blank=True,null=True)
    amount= models.IntegerField(max_length=100,null=True)
    withdraw=models.IntegerField(max_length=100,null=True) 
    account= models.IntegerField(max_length=100,null=True)
    add_money= models.IntegerField(max_length=100,null=True)
    withdraw  = models.IntegerField(max_length=100,null=True)
    id = models.UUIDField(unique=True, primary_key=True, editable=True)
    
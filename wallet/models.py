from django.db import models

# Create your models here.
class Register(models.Model):
    mobile=models.IntegerField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,blank=True)
    name=models.CharField(max_length=100,blank=True)

class Login(models.Model):
    mobile=models.IntegerField(max_length=100,null=True)
    otp=models.IntegerField(max_length=100,blank=True,null=True)
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Person)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['mobile','otp','name','Balance','email','marks']

@admin.register(wallet)  
class WalletAdmin(admin.ModelAdmin):
    list_display=['use',]

@admin.register(bank)
class BankAdmin(admin.ModelAdmin):
    list_display=['account_number','send_money']      

   
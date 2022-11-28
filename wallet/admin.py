from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Person)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['mobile','otp','name','Balance']

@admin.register(wallet)  
class WalletAdmin(admin.ModelAdmin):
    list_display=['use']  

# @admin.register(Register)
# class LoginAdmin(admin.ModelAdmin):
#     list_display=['mobile','email']   

# @admin.register(balance)
# class BalanceAdmin(admin.ModelAdmin):
#     list_display=['admin','account','amount','Balance']    
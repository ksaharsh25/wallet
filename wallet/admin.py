from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Person)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['mobile','otp','name','account_number']

@admin.register(wallet)  
class WalletAdmin(admin.ModelAdmin):
    list_display=['Balance','add_money','withdraw']  

# @admin.register(Register)
# class LoginAdmin(admin.ModelAdmin):
#     list_display=['mobile','email']   

# @admin.register(balance)
# class BalanceAdmin(admin.ModelAdmin):
#     list_display=['admin','account','amount','Balance']    

from django import forms
from django.forms import ModelForm
from .models import *

# class WalletForm(ModelForm):
#     class Meta:
#         model = wallet
        
#         fields = ('Balance',)

#         widgets = {
            
#             'Balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
          
            
        # }
# class PersonForm(ModelForm):
#     class Meta:
#         model=Person
#         widgets = {
            
#             'Balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
#             'add_money': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add_money'}),
#             'withdraw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'withdraw'}),
            
#         }
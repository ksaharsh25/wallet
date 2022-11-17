
from django import forms
from django.forms import ModelForm
from .models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = wallet
        
        fields = (  'add_money', 'withdraw')

        widgets = {
            
            'Balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
            'add_money': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add_money'}),
            'withdraw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'withdraw'}),
            
        }

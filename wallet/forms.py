from django import forms
from django.forms import ModelForm
from .models import *
class EmployeeForm(ModelForm):
    class Meta:
        model = Login
        fields = ('mobile','name','account','Balance')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'account'}),
            'Balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
            'mobile':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobile'}),
        }
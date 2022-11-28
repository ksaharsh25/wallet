from rest_framework import serializers
from .models import *

class API(serializers.ModelSerializer):
    class Meta:
        model=wallet
        fields=('use',)

class API(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('account_number','Balance')
       
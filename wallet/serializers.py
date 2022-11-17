from rest_framework import serializers
from .models import *

class API(serializers.ModelSerializer):
    class Meta:
        model=wallet
        fields=('use','Balance','add_money','account_number','withdraw')

class API(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('account_number','Balance','add_money')
       
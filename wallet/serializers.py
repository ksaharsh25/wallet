from rest_framework import serializers
from .models import *

class API(serializers.ModelSerializer):
    class Meta:
        model=wallet
        fields=('user','Balance','add_money','account','withdraw')


       
from rest_framework import serializers
from .models import *

class API(serializers.ModelSerializer):
    class Meta:
        model=balance
        fields=('admin','balance','id','account')


       
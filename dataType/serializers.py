from rest_framework import serializers
from .models import DataType
from django.conf import settings

class DataTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataType
        fields = ('__all__') 

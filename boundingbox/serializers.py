from rest_framework import serializers
from .models import boundingBox
from django.conf import settings

class boundingBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = boundingBox
        fields = ('__all__') 

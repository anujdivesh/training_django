from rest_framework import serializers
from .models import SpatialRepresentationInfo
from django.conf import settings

class SpatialRepresentationInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpatialRepresentationInfo
        fields = ('__all__') 

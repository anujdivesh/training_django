from rest_framework import serializers
from .models import Project
from django.conf import settings

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__') 

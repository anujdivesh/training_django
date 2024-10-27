from rest_framework import serializers
from .models import Topic
from django.conf import settings

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('__all__') 

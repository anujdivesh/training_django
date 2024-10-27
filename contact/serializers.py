from rest_framework import serializers
from .models import Contact
from django.conf import settings

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('__all__') 

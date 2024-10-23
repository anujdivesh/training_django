from rest_framework import serializers
from .models import Dataset
from django.conf import settings

class DatasetSerializer(serializers.ModelSerializer):
    full_file_path = serializers.SerializerMethodField()

    class Meta:
        model = Dataset
        fields = ('title','abstract','file','full_file_path') 


        
    def get_full_file_path(self, obj):
        request = self.context.get('request')  # Get the request from context
        if request and obj.file:
            return request.build_absolute_uri(obj.file.url)  # Construct the full URL
        return None  # Return None if there is no file
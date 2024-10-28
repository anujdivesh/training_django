from rest_framework import serializers
from .models import Dataset
from django.conf import settings

class DatasetSerializer(serializers.ModelSerializer):
    full_file_path = serializers.SerializerMethodField()

    class Meta:
        model = Dataset
        fields = ('id','title','abstract','temporalCoverageFrom','temportalCoverageTo',\
        'language','version','openAccess','dataType','project','SpatialInfo',\
        'autoGenerateBBOX','boundingBox','GeoReferenceSystem','contact','publisher',\
        'license','Tag','Topic','LocalAccessPath','file','full_file_path','created_at','updated_at') 
        depth = 3

        
    def get_full_file_path(self, obj):
        request = self.context.get('request')  # Get the request from context
        if request and obj.file:
            return request.build_absolute_uri(obj.file.url)  # Construct the full URL
        return None  # Return None if there is no file
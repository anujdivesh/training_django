from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Dataset
from .serializers import DatasetSerializer  
from .permissions import IsAuthenticatedForPOSTOnly
from django.shortcuts import get_object_or_404

def datasets(request):
    return HttpResponse("Hello world!")

class DatasetView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Dataset.objects.all()

    def list(self, request):
        queryset = self.queryset  # Use the class-level queryset
        # Get query parameters
        openAccess_id = request.query_params.get('openAccess', None)
        data_type_id = request.query_params.get('dataType', None)
        project_id = request.query_params.get('project', None)
        spatial_info_id = request.query_params.get('SpatialInfo', None)
        tag_id = request.query_params.get('Tag', None)
        topic_id = request.query_params.get('Topic', None)
        # Apply filters only if parameters are provided
        if data_type_id == 'all' or data_type_id is None:
            pass
        elif data_type_id:
            queryset = queryset.filter(dataType_id=data_type_id)

        if project_id == 'all' or project_id is None:
            pass
        elif project_id:
            queryset = queryset.filter(project__id=project_id)

        if spatial_info_id == 'all' or spatial_info_id is None:
            pass
        elif spatial_info_id:
            queryset = queryset.filter(SpatialInfo_id=spatial_info_id)

        if openAccess_id == 'all' or openAccess_id is None:
            pass
        elif openAccess_id:
            queryset = queryset.filter(openAccess=openAccess_id)

        if tag_id == 'all' or tag_id is None:
            pass
        elif tag_id:
            queryset = queryset.filter(Tag=tag_id)

        if topic_id == 'all' or topic_id is None:
            pass
        elif topic_id:
            queryset = queryset.filter(Topic=topic_id)
        
        # Serialize the filtered queryset
        #serializer = DatasetSerializer(queryset, many=True)
        serializer = DatasetSerializer(queryset, many=True, context={'request': request})  # Pass the request context
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Dataset.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DatasetSerializer(user)
        return Response(serializer.data)
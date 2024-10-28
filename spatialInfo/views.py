from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import SpatialRepresentationInfo
from .serializers import SpatialRepresentationInfoSerializer  
from .permissions import IsAuthenticatedForPOSTOnly

def spatialrepresentationinfos(request):
    return HttpResponse("Hello world!")

class SpatialRepresentationInfoView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = SpatialRepresentationInfo.objects.all()

    def list(self, request):
        queryset = SpatialRepresentationInfo.objects.all()
        serializer = SpatialRepresentationInfoSerializer(queryset, many=True)
        return Response(serializer.data)
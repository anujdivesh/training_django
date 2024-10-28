from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import boundingBox
from .serializers import boundingBoxSerializer  
from .permissions import IsAuthenticatedForPOSTOnly

def boundingBoxs(request):
    return HttpResponse("Hello world!")

class boundingBoxView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = boundingBox.objects.all()

    def list(self, request):
        queryset = boundingBox.objects.all()
        serializer = boundingBoxSerializer(queryset, many=True)
        return Response(serializer.data)
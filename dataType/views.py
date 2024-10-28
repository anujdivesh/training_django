from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import DataType
from .serializers import DataTypeSerializer  
from .permissions import IsAuthenticatedForPOSTOnly

def datatypes(request):
    return HttpResponse("Hello world!")

class DataTypeView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = DataType.objects.all()

    def list(self, request):
        queryset = DataType.objects.all()
        serializer = DataTypeSerializer(queryset, many=True)
        return Response(serializer.data)
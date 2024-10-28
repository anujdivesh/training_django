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


def datasets(request):
    return HttpResponse("Hello world!")

class DatasetView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Dataset.objects.all()

    def list(self, request):
        queryset = self.queryset  # Use the class-level queryset
        serializer = DatasetSerializer(queryset, many=True, context={'request': request})  # Pass the request context
        return Response(serializer.data)
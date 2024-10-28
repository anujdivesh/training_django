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
from django.shortcuts import get_object_or_404

def boundingBoxs(request):
    return HttpResponse("Hello world!")

class boundingBoxView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = boundingBox.objects.all()

    def list(self, request):
        queryset = boundingBox.objects.all()
        serializer = boundingBoxSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = boundingBox.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = boundingBoxSerializer(user)
        return Response(serializer.data)
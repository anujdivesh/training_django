from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer  
from .permissions import IsAuthenticatedForPOSTOnly

def tags(request):
    return HttpResponse("Hello world!")

class TagView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Tag.objects.all()

    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)
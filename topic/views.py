from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Topic
from .serializers import TopicSerializer  

def topics(request):
    return HttpResponse("Hello world!")

class TopicView(viewsets.ViewSet):
    queryset = Topic.objects.all()

    def list(self, request):
        queryset = Topic.objects.all()
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)
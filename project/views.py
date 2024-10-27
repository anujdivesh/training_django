from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer  

def projects(request):
    return HttpResponse("Hello world!")

class ProjectView(viewsets.ViewSet):
    queryset = Project.objects.all()

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
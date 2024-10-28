from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer  
from .permissions import IsAuthenticatedForPOSTOnly
from django.shortcuts import get_object_or_404

def projects(request):
    return HttpResponse("Hello world!")

class ProjectView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Project.objects.all()

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(user)
        return Response(serializer.data)
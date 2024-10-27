from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer  

def ContactBoxs(request):
    return HttpResponse("Hello world!")

class ContactView(viewsets.ViewSet):
    queryset = Contact.objects.all()

    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)
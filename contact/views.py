from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer  
from .permissions import IsAuthenticatedForPOSTOnly
from django.shortcuts import get_object_or_404

def ContactBoxs(request):
    return HttpResponse("Hello world!")

class ContactView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Contact.objects.all()

    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contact.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ContactSerializer(user)
        return Response(serializer.data)
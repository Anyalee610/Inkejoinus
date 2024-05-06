from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import JoinUs
from .serializers import JoinUsSerializer



class JoinUsView(generics.ListCreateAPIView):
    # Specify the queryset containing the objects this view will work with
    queryset = JoinUs.objects.all()
    
    # Specify the serializer class that will handle conversion between JSON and Python objects
    serializer_class = JoinUsSerializer

    # def post(self, request):

    #     serializer = JoinUsSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
        

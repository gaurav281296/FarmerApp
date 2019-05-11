from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import farmer
from . serializers import farmerSerializer

class farmerList(APIView):

    def get(self, request):
        farmers = farmer.objects.all()
        serializedFarmers = farmerSerializer(farmers, many=True)
        return Response(serializedFarmers.data)
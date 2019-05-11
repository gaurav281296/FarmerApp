from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import farmer as farmermodel
from . serializers import farmerSerializer


@api_view(['GET', 'POST'])
def farmer_list(request, format=None):
    if request.method == 'GET':
        farmers = farmermodel.objects.all()
        serializedFarmers = farmerSerializer(farmers, many=True)
        return Response(serializedFarmers.data)
    elif request.method == 'POST':
        farmer = request.data.get('farmer')
        serializedFarmers = farmerSerializer(data = farmer)
        if serializedFarmers.is_valid(raise_exception = True):
            farmer_saved = serializedFarmers.save()
        return Response({"success": "Farmer '{}' added successfully".format(farmer_saved)})


@api_view(['GET','PUT','DELETE'])
def farmer_detail(request, id, format=None):
        try:
            farmer = farmermodel.objects.get(pk=id)
        except farmer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializedFarmers = farmerSerializer(farmer)
            return Response(serializedFarmers.data)

        elif request.method == 'PUT':
            serializedFarmers = farmerSerializer(farmer, data = request.data)
            if serializedFarmers.is_valid(raise_exception = True):
                farmer_saved = serializedFarmers.save()
            return Response({"success": "Farmer '{}' modified successfully".format(farmer_saved)})

        elif request.method == 'DELETE':
            farmer.delete()
            return Response({"message": "Farmer with id `{}` has been deleted.".format(id)},status=204)

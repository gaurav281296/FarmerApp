from django.shortcuts import render

# Create your views here.
from . models import farmer as farmermodel
from farm.models import farm as farmmodel
from . serializers import farmerSerializer
from farm.serializers import farmSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

class farmerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = farmermodel.objects.filter(pk=0)    #we don't make use of queryset because user can switch at anytime. save memory by asking for only a single object
    serializer_class = farmerSerializer
    def get(self, request, *args, **kwargs):
        farmers = farmerSerializer.getAll(request.user.id)
        return Response(farmers.data)

    def post(self, request, *args, **kwargs):
        farmer = farmerSerializer.createFarmer(request.user.id,request.data)
        return Response(farmer.data)


class farmerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = farmermodel.objects.all() #objects.get(pk=id)
    serializer_class = farmerSerializer

    def get(self, request, *args, **kwargs):
        farmer_id = kwargs['pk']
        farmer = farmerSerializer.getById(request.user.id, farmer_id)
        return Response(farmer.data)

    def put(self, request, *args, **kwargs):
        farmer_id = kwargs['pk']
        farmer = farmerSerializer.updateFarmer(request.user.id,farmer_id,request.data)
        return Response(farmer.data)

    def delete(self, request, *args, **kwargs):
        farmer_id = kwargs['pk']
        farmer = farmerSerializer.deleteById(request.user.id,farmer_id)
        return Response(farmer)
        #return self.destroy(request, *args, **kwargs)

@api_view(['GET'])
def farmerQuery(request, cropGrown, format=None):
    #get all farms that grow the crop
    farms_dict = farmSerializer.getByCropGrown(cropGrown).data
    #get their owner id's
    owners = []
    for owner in farms_dict:
        owners.append(int(owner['Owner']))
    farmers = farmerSerializer.getFarmersByIds(owners)
    return Response(farmers.data)
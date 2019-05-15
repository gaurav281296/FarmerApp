from django.shortcuts import render

# Create your views here.
from . models import farmer as farmermodel
from farm.models import farm as farmmodel
from . serializers import farmerSerializer
from farm.serializers import farmSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

class farmerList(APIView):
    def get(self, request, *args, **kwargs):
        user_country = userprofileSerializer.getProfileByUserId(self.request.user.id).data['country']
        famers = farmerSerializer.getAll(user_country)
        return Response(farmers.data)
    
    def post(self, request, *args, **kwargs):
        user_country = userprofileSerializer.getProfileByUserId(self.request.user.id).data['country']
        farmer = farmerSerializer(data=request.data)
        if farmer.is_valid():
            farmer.save(using=user_country)
            return Response(farmer.data, status=status.HTTP_201_CREATED)
        return Response(farmer.errors, status=status.HTTP_400_BAD_REQUEST)


class farmerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = farmermodel.objects.all() #objects.get(pk=id)
    serializer_class = farmerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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
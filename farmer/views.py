from django.shortcuts import render

# Create your views here.
from . models import farmer as farmermodel
from farm.models import farm as farmmodel
from . serializers import farmerSerializer
from farm.serializers import farmSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class farmerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = farmermodel.objects.all()
    serializer_class = farmerSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
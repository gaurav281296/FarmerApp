from django.shortcuts import render

# Create your views here.
from . models import farmer as farmermodel
from farm.models import farm as farmmodel
from . serializers import farmerReadSerializer, farmerWriteSerializer
from farm.serializers import farmQuerySerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class farmerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = farmermodel.objects.all()
    serializer_class = farmerReadSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class farmerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = farmermodel.objects.all() #objects.get(pk=id)
    serializer_class = farmerWriteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(['GET'])
def farmQuery(request, CropGrown, format=None):
    farms_got = farmmodel.objects.filter(CropGrown=CropGrown).distinct()
    owners_dict = farmQuerySerializer(farms_got, many=True).data
    owners = []
    for owner in owners_dict:
        owners.append(int(owner['Owner']))
    farm_owners=farmermodel.objects.filter(id__in=owners)
    owners_dict = farmerWriteSerializer(farm_owners,many=True).data
    return Response(owners_dict)
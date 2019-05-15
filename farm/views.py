from django.shortcuts import render
# Create your views here.
from . models import farm as farmmodel
from . serializers import farmSerializer #returns all fields
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

#mixins handle exceptions automatically
class farmList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = farmmodel.objects.all()
    serializer_class = farmSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
#mixins handle exceptions automatically
class farmDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = farmmodel.objects.all()
    serializer_class = farmSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(['GET'])
def farmQuery(request, farmerId, format=None):
    farms = farmSerializer.getByFarmerId(farmerId)
    return Response(farms.data)
from django.shortcuts import render
# Create your views here.
from . models import farm as farmmodel
from . serializers import farmWriteSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class farmList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = farmmodel.objects.all()
    serializer_class = farmWriteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class farmDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = farmmodel.objects.all() #objects.get(pk=id)
    serializer_class = farmWriteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(['GET'])
def farmQuery(request, farmerId, format=None):
    farms = farmmodel.objects.filter(Owner=farmerId)
    farms = farmWriteSerializer(farms, many=True).data
    return Response(farms)
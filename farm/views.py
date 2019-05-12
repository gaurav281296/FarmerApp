from django.shortcuts import render
# Create your views here.
from . models import farm as farmmodel
from . serializers import farmWriteSerializer, farmReadSerializer
from rest_framework import mixins
from rest_framework import generics

class farmList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = farmmodel.objects.all()
    serializer_class = farmReadSerializer

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
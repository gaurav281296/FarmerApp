from django.shortcuts import render

# Create your views here.
from . models import farmer as farmermodel
from . serializers import farmerReadSerializer, farmerWriteSerializer
from rest_framework import mixins
from rest_framework import generics

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
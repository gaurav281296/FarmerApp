from django.shortcuts import render
# Create your views here.
from . models import fertilizer as fertilizermodel
from . serializers import fertilizerSerializer
from rest_framework import mixins
from rest_framework import generics

#mixins handle exceptions automatically
class fertilizerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = fertilizermodel.objects.all()
    serializer_class = fertilizerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#mixins handle exceptions automatically
class fertilizerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = fertilizermodel.objects.all() #objects.get(pk=id)
    serializer_class = fertilizerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
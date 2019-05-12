from django.shortcuts import render

# Create your views here.
from . models import schedule as schedulemodel
from . serializers import scheduleSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response

class scheduleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = schedulemodel.objects.all()
    serializer_class = scheduleSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        if(request.data['Unit'] not in ["kg","g","l","ml"]):
            return Response("Unit should be either kg, g, l or ml only")
        return self.create(request, *args, **kwargs)


class scheduleDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = schedulemodel.objects.all() #objects.get(pk=id)
    serializer_class = scheduleSerializer

    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
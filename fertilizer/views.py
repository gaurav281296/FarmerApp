from django.shortcuts import render
# Create your views here.
from . models import fertilizer as fertilizermodel
from . serializers import fertilizerSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class fertilizerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = fertilizermodel.objects.all()
    serializer_class = fertilizerSerializer

    def get(self, request, *args, **kwargs):
        fertilizer = fertilizerSerializer.getAll(request.user.id)
        return Response(fertilizer.data)

    def post(self, request, *args, **kwargs):
        fertilizer = fertilizerSerializer.createFertilizer(request.user.id,request.data)
        return Response(fertilizer.data)

class fertilizerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = fertilizermodel.objects.all() #objects.get(pk=id)
    serializer_class = fertilizerSerializer

    def get(self, request, *args, **kwargs):
        fertilizer_id = kwargs['pk']
        fertilizer = fertilizerSerializer.getById(request.user.id, fertilizer_id)
        return Response(fertilizer.data)

    def put(self, request, *args, **kwargs):
        fertilizer_id = kwargs['pk']
        fertilizer = fertilizerSerializer.updateFertilizer(request.user.id,fertilizer_id,request.data)
        return Response(fertilizer.data)

    def delete(self, request, *args, **kwargs):
        fertilizer_id = kwargs['pk']
        fertilizer = fertilizerSerializer.deleteById(request.user.id,fertilizer_id)
        return Response(fertilizer)
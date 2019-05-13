from django.shortcuts import render

# Create your views here.
from . models import schedule as schedulemodel
from farm.models import farm as farmmodel
from farm.serializers import farmScheduleSerializer
from . serializers import scheduleSerializer, scheduleQuerySerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date,timedelta

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

@api_view(['GET'])
def scheduleQuery(request, format=None):
    schedules_due=[]
    tomorrow = date.today() + timedelta(days=1)
    farms_present = farmmodel.objects.all()
    farms_dict = farmScheduleSerializer(farms_present,many=True).data
    for farms in farms_dict:
        for schedule in farms['Schedules']: #iterates over schedules of farms having schedules
            DaysAfterSowing = scheduleQuerySerializer(schedulemodel.objects.get(pk=schedule)).data['DaysAfterSowing']
            scheduled_date = date(*map(int,farms['SowingDate'].split('-'))) + timedelta(days=int(DaysAfterSowing))
            days_diff = (scheduled_date - tomorrow).days
            if (days_diff >= 0 and days_diff < 2): #schedules whose deadlines have passed don't appear here
                schedules_due.append(int(schedule))
    
    schedules = schedulemodel.objects.filter(id__in=schedules_due)
    schedules_dict = scheduleSerializer(schedules, many=True).data
    return Response(schedules_dict)

@api_view(['GET'])
def scheduleByFarm(request, farmId, format=None):
    schedules = schedulemodel.objects.filter(Farm = farmId)
    schedules = scheduleSerializer(schedules,many=True).data
    return Response(schedules)
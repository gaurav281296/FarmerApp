from django.shortcuts import render

# Create your views here.
from . models import schedule as schedulemodel
from farm.serializers import farmScheduleSerializer
from . serializers import scheduleSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date,timedelta

tomorrow = date.today() + timedelta(days=1)

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
def scheduleByFarm(request, farmId, format=None):
    schedules = scheduleSerializer.getSchedulesByFarmId(farmId)
    return Response(schedules.data)


@api_view(['GET'])
def scheduleQuery(request, format=None):
    #print(request.user.id)
    schedules_due=[]
    allFarms = farmScheduleSerializer.getAllFarms().data
    
    for farms in allFarms:
        for schedule in farms['Schedules']: #iterates over schedules of farms having schedules
            daysAfterSowing = scheduleSerializer.getScheduleById(schedule).data['DaysAfterSowing']
            scheduled_date = date(*map(int,farms['SowingDate'].split('-'))) + timedelta(days=int(daysAfterSowing))
            days_diff = (scheduled_date - tomorrow).days + 1 #time delta is math.floor
            if (days_diff >= 0 and days_diff < 2): #expired schedules don't appear here
                schedules_due.append(int(schedule))
    
    schedules_dict = scheduleSerializer.getSchedulesByIds(schedules_due)
    return Response(schedules_dict.data)
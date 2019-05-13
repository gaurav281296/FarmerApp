from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from farmer.models import farmer as farmermodel
from farm.models import farm as farmmodel
from schedule.models import schedule as schedulemodel
from fertilizer.models import fertilizer as fertilizermodel
from farm.serializers import farmScheduleSerializer
from farmer.serializers import farmerReadSerializer
from schedule.serializers import scheduleSerializer
from fertilizer.serializers import fertilizerSerializer
import json

class bom_entry():
    def __init__(self, schedule_id, fertilizer_name, cost_per_g_or_ml, quantity_in_g_or_ml, schedule_cost):
        self.schedule_id = schedule_id
        self.fertilizer_name = fertilizer_name
        self.cost_per_g_or_ml = cost_per_g_or_ml
        self.quantity_in_g_or_ml = quantity_in_g_or_ml
        self.schedule_cost = schedule_cost

class billofmaterial():
    def __init__(self, bom, final_cost):
        self.bom = bom
        self.final_cost = final_cost
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        

#enter validation checks and 404 errors
@api_view(['GET'])
def bom(request, farmerId, format=None):
    total_cost = 0.0
    farmer = farmermodel.objects.get(pk=farmerId)
    farms_owned = farmerReadSerializer(farmer).data['Farms'] #get pk's of farms owned
    farms = farmmodel.objects.filter(id__in=farms_owned)
    farms = farmScheduleSerializer(farms, many=True).data
    schedules = []
    boms = []
    for farm in farms:
        for schedule in farm['Schedules']: #get pk's of schedules of the farms
            schedules.append(int(schedule))
    schedules = schedulemodel.objects.filter(id__in=schedules)
    schedules = scheduleSerializer(schedules, many=True).data
    for schedule in schedules: #calculate the cost based on fertilizer's cost
        schedule_id = schedule['id']
        unit = schedule['Unit']
        quantity = float(schedule['Quantity'])
        fertilizer = fertilizermodel.objects.get(pk=schedule['Fertilizer']) #get details of the fertilizer to get it's cost
        fertilizer_name = fertilizerSerializer(fertilizer).data['Name']
        si_unit_cost = float(fertilizerSerializer(fertilizer).data['PricePerSIunit'])
        cost_per_g_or_ml = si_unit_cost/1000
        if(unit == 'kg' or unit == 'l'):    #convert quantityy to gramas or ml
            quantity = quantity*1000
        cost = cost_per_g_or_ml*quantity
        bom_entry_temp = bom_entry(schedule_id, fertilizer_name, cost_per_g_or_ml, quantity,cost)
        boms.append(bom_entry_temp)
        total_cost = total_cost + cost
    bom_final = billofmaterial(boms,total_cost)
    bom_final = bom_final.toJson()
    return Response(json.loads(bom_final))
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from farm.serializers import farmScheduleSerializer
from farmer.serializers import farmerReadSerializer
from schedule.serializers import scheduleSerializer
from fertilizer.serializers import fertilizerSerializer
import json

class bom_entry():
    def __init__(self, schedule_id, fertilizer_name, cost_per_g_or_ml, quantity_in_g_or_ml, schedule_cost):
        self.schedule_id = schedule_id
        self.fertilizer = fertilizer_name
        self.cost_per_g_or_ml = cost_per_g_or_ml
        self.quantity_in_g_or_ml = quantity_in_g_or_ml
        self.schedule_cost = schedule_cost

class billofmaterial():
    def __init__(self, bom, final_cost):
        self.bom = bom
        self.final_cost = final_cost
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        


@api_view(['GET'])
def BillOfMaterial(request, farmerId, format=None):
    total_cost = 0.0
    #get farm_ids owned by a farmer using his farmerId
    farms_owned = farmerReadSerializer.getFarmerById(farmerId).data['Farms']
    #get farms by ids
    farms = farmScheduleSerializer.getFarmsByIds(farms_owned).data
    schedules = []
    boms = []
    #get all schedule ids of the farms owned by the farmer
    for farm in farms:
        for schedule in farm['Schedules']: #get pk's of schedules of the farms
            schedules.append(int(schedule))

    #get schedules by ids
    schedules = scheduleSerializer.getSchedulesByIds(schedules).data
    for schedule in schedules: #calculate the cost based on fertilizer's cost
        
        schedule_id = schedule['id']
        unit = schedule['Unit']
        quantity = float(schedule['Quantity'])
        fertilizer = fertilizerSerializer.getFertilizerById(schedule['Fertilizer']).data
        fertilizer_name = fertilizer['Name']
        si_unit_cost = float(fertilizer['PricePerSIunit'])

        cost_per_g_or_ml = si_unit_cost/1000
        if(unit == 'kg' or unit == 'l'):    #convert quantityy to gramas or ml
            quantity = quantity*1000
        
        cost = cost_per_g_or_ml*quantity
        
        boms.append(bom_entry(schedule_id, fertilizer_name, cost_per_g_or_ml, quantity,cost))
        total_cost = total_cost + cost

    bom_final = billofmaterial(boms,total_cost)
    bom_final = bom_final.toJson()
    return Response(json.loads(bom_final))
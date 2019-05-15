from rest_framework import serializers
from . models import schedule as schedulemodel

class scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = schedulemodel
        fields = '__all__'
        
    def create(self, validated_data):
        return schedulemodel.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.DaysAfterSowing = validated_data.get('DaysAfterSowing', instance.DaysAfterSowing)
        instance.Fertilizer = validated_data.get('Fertilizer', instance.Fertilizer)
        instance.Quantity = validated_data.get('Quantity', instance.Quantity)
        instance.Unit = validated_data.get('Unit', instance.Unit)
        instance.Farm = validated_data.get('Farm', instance.Farm)
        instance.save()
        return instance
    
    def getScheduleById(scheduleId):
        schedule = schedulemodel.objects.get(pk=scheduleId)
        return scheduleSerializer(schedule)
    
    def getSchedulesByIds(ids):
        schedules = schedulemodel.objects.filter(id__in=ids)
        return scheduleSerializer(schedules,many=True)
    
    def getSchedulesByFarmId(farmId):
        schedules = schedulemodel.objects.filter(Farm=farmId)
        return scheduleSerializer(schedules,many=True)
from rest_framework import serializers
from . models import farm as farmmodel

class farmSerializer(serializers.ModelSerializer):
    class Meta:
        model = farmmodel
        fields = '__all__'
    
    def create(self, validated_data):
        return farmmodel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Area = validated_data.get('Area', instance.Area)
        instance.Village = validated_data.get('Village', instance.Village)
        instance.CropGrown = validated_data.get('CropGrown', instance.CropGrown)
        instance.SowingDate = validated_data.get('SowingDate', instance.SowingDate)
        instance.Owner = validated_data.get('Owner', instance.Owner)
        instance.save()
        return instance
    
    def getByFarmerId(farmerId):
        farms = farmmodel.objects.filter(Owner=farmerId)
        return farmSerializer(farms,many=True)
    
    def getByCropGrown(cropGrown):
        farms = farmmodel.objects.filter(CropGrown=cropGrown).distinct()
        return farmSerializer(farms,many=True)

class farmScheduleSerializer(serializers.ModelSerializer):
    Schedules = serializers.StringRelatedField(many=True)
    class Meta:
        model = farmmodel
        fields = ('Schedules','SowingDate')
    
    def getAllFarms():
        farms = farmmodel.objects.all()
        return farmScheduleSerializer(farms,many=True)

    def getFarmsByIds(ids):
        farms = farmmodel.objects.filter(id__in=ids)
        return farmScheduleSerializer(farms,many=True)
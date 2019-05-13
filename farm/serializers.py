from rest_framework import serializers
from . models import farm as farmmodel

class farmWriteSerializer(serializers.ModelSerializer):
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

class farmReadSerializer(serializers.ModelSerializer):
    Schedules = serializers.StringRelatedField(many=True)
    class Meta:
        model = farmmodel
        fields = '__all__'

class farmQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = farmmodel
        fields = [('Owner')]

class farmScheduleSerializer(serializers.ModelSerializer):
    Schedules = serializers.StringRelatedField(many=True)
    class Meta:
        model = farmmodel
        fields = ('Schedules','SowingDate')
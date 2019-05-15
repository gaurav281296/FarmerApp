from rest_framework import serializers
from . models import farmer as farmermodel

class farmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = farmermodel
        fields = '__all__'
        
    def create(self, validated_data):
        return farmermodel.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.PhoneNumber = validated_data.get('PhoneNumber', instance.PhoneNumber)
        instance.Language = validated_data.get('Language', instance.Language)
        instance.save()
        return instance

    def getFarmersByIds(ids):
        farmers = farmermodel.objects.filter(id__in=ids)
        return farmerSerializer(farmers,many=True)

class farmerReadSerializer(serializers.ModelSerializer):
    Farms = serializers.StringRelatedField(many=True)
    class Meta:
        model = farmermodel
        fields = '__all__'
    
    def getFarmerById(farmerId):
        farmer = farmermodel.objects.get(pk=farmerId)
        return farmerReadSerializer(farmer)
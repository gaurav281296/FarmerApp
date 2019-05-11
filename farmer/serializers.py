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
        instance.Farm = validated_data.get('Farm', instance.Farm)
        instance.save()
        return instance
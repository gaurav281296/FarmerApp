from rest_framework import serializers
from . models import fertilizer as fertilizermodel

class fertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = fertilizermodel
        fields='__all__'
    
    def create(self, validated_data):
        return fertilizermodel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.PricePerSIunit = validated_data.get('PricePerSIunit', instance.PricePerSIunit)
        instance.save()
        return instance
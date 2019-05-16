from rest_framework import serializers
from . models import fertilizer as fertilizermodel
from userprofile.serializers import userprofileSerializer
from rest_framework import status

def get_country(userId):
    return userprofileSerializer.getProfileByUserId(userId).data['country']

def get_fertilizer(user_country, fertilizerId):
    try:
        return fertilizermodel.objects.using(user_country).get(pk=fertilizerId)
    except fertilizermodel.DoesNotExist:
        return status.HTTP_404_NOT_FOUND

class fertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = fertilizermodel
        fields='__all__'
    
    def createFertilizer(userId,fertilizer_data):
        user_country = get_country(userId)
        fertilizer = fertilizermodel(Name=fertilizer_data['Name'], PricePerSIunit=fertilizer_data['PricePerSIunit'])
        fertilizer.save(using=user_country,force_insert=True)
        return fertilizerSerializer(fertilizer)
    
    def getAll(userId):
        user_country = get_country(userId)
        fertilizer = fertilizermodel.objects.using(user_country).all()
        return fertilizerSerializer(fertilizer,many=True)

    def getById(userId, fertilizerId):
        user_country = get_country(userId)
        fertilizer = get_fertilizer(user_country,fertilizerId)
        return fertilizerSerializer(fertilizer)
    
    def updateFertilizer(userId, fertilizerId, fertilizer_data):
        user_country = get_country(userId)
        fertilizer = get_fertilizer(user_country,fertilizerId)
        fertilizer = fertilizerSerializer(fertilizer,data=fertilizer_data)
        if fertilizer.is_valid():
            fertilizer.save()
        return fertilizer
    
    def deleteById(userId,fertilizerId):
        user_country = get_country(userId)
        fertilizer = get_fertilizer(user_country,fertilizerId)
        if fertilizer==404:
            return status.HTTP_404_NOT_FOUND
        fertilizer.delete()
        return status.HTTP_204_NO_CONTENT
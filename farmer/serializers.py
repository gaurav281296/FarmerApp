from rest_framework import serializers
from . models import farmer as farmermodel
from userprofile.serializers import userprofileSerializer
from rest_framework import status

def get_country(userId):
    return userprofileSerializer.getProfileByUserId(userId).data['country']

def get_farmer(user_country, farmerId):
    try:
        return farmermodel.objects.using(user_country).get(pk=farmerId)
    except farmermodel.DoesNotExist:
        return status.HTTP_404_NOT_FOUND

class farmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = farmermodel
        fields = '__all__'

    def createFarmer(userId,farmer_data):
        user_country = get_country(userId)
        farmer = farmermodel(Language=farmer_data['Language'], Name=farmer_data['Name'],PhoneNumber=farmer_data['PhoneNumber'])
        farmer.save(using=user_country,force_insert=True)
        return farmerSerializer(farmer)
    
    def getAll(userId):
        user_country = get_country(userId)
        farmers = farmermodel.objects.using(user_country).all()
        return farmerSerializer(farmers,many=True)

    def getById(userId, farmerId):
        user_country = get_country(userId)
        farmer = get_farmer(user_country,farmerId)
        return farmerSerializer(farmer)
    
    def updateFarmer(userId, farmerId, farmer_data):
        user_country = get_country(userId)
        farmer = get_farmer(user_country,farmerId)
        farmer = farmerSerializer(farmer,data=farmer_data)
        if farmer.is_valid():
            farmer.save()
        return farmer
    
    def deleteById(userId,farmerId):
        user_country = get_country(userId)
        farmer = get_farmer(user_country,farmerId)
        if farmer==404:
            return status.HTTP_404_NOT_FOUND
        farmer.delete()
        return status.HTTP_204_NO_CONTENT

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
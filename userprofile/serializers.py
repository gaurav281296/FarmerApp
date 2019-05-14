from rest_framework import serializers
from . models import userprofile as userprofilemodel

class userprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofilemodel
        fields = '__all__'
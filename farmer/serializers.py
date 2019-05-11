from rest_framework import serializers
from . models import farmer

class farmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = farmer
        #fields = ('Name', 'PhoneNumber', 'Language')
        fields = '__all__'

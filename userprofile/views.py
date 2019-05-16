from django.shortcuts import render
from userprofile.models import User
from userprofile.models import userprofile as userprofilemodel
from userprofile.serializers import userprofileSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
#using=self._db

@api_view(['PUT'])
def userprofileUpdate(request, country, format=None):
    userId = request.user.id
    user = User.objects.get(pk=userId)
    user.userprofile.country = country
    user.save()
    userprofile = userprofilemodel.objects.get(pk=userId)#proxy query
    userprofile = userprofileSerializer(userprofile) #serialized
    return Response(userprofile.data) #return serialized
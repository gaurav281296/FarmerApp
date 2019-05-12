from django.db import models
from farmer.models import farmer
# Create your models here.
class farm(models.Model):
    Area = models.IntegerField()
    Village = models.CharField(max_length=20)
    CropGrown = models.CharField(max_length=20)
    SowingDate = models.DateField()
    Owner = models.ForeignKey(farmer,related_name='Farms',default=0,on_delete=models.SET_DEFAULT)
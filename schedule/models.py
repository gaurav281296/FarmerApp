from django.db import models
from fertilizer.models import fertilizer
from farm.models import farm
from enum import Enum

# Create your models here.
class schedule(models.Model):
    DaysAfterSowing = models.PositiveIntegerField()
    Fertilizer = models.ForeignKey(fertilizer,default=0,on_delete=models.SET_DEFAULT)
    Quantity = models.DecimalField(max_digits=6,decimal_places=2)
    Unit = models.CharField(max_length=3)
    Farm = models.ForeignKey(farm,related_name='Schedules',default=0,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return '{0}'.format(self.id)
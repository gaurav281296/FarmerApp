from django.db import models
from farm.models import farm
# Create your models here.
class farmer(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=15)
    Language = models.CharField(max_length=20)
    Farm = models.ForeignKey(farm,default=0,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.Name

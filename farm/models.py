from django.db import models

# Create your models here.
class farm(models.Model):
    Area = models.IntegerField()
    Village = models.CharField(max_length=20)
    CropGrown = models.CharField(max_length=20)
    SowingDate = models.DateField()
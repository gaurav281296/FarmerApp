from django.db import models

# Create your models here.
class farmer(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=15)
    Language = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

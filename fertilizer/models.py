from django.db import models

# Create your models here.
class fertilizer(models.Model):
    Name = models.CharField(max_length=20)
    PricePerSIunit = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return '{0}'.format(self.Name)
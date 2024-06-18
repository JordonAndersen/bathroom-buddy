from django.db import models

# Create your models here.

class Restroom(models.Model):
    
    name = models.CharField(blank=False, null=False, max_length=255)
    address = models.CharField(blank=False, null=False, max_length=255)
    latitude = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=6)
    longitude  = models.DecimalField(blank=False, null=False, max_digits=9, decimal_places=6)
    time_created = models.DateTimeField(blank=False, null=False)

    def __str__(self) -> str:
        return f'Restroom name: {self.name}, Address: {self.address}'
    
    
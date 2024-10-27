from django.db import models

# Create your models here.
class boundingBox(models.Model):
   island_name = models.CharField(max_length=255)
   westBoundLongitude = models.FloatField()
   eastBoundLongitude = models.FloatField()
   southBoundLatitude = models.FloatField()
   northBoundLatitude = models.FloatField()

   def __str__(self):
        return self.island_name
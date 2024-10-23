from django.db import models
from anchor.models.fields import BlobField


class Dataset(models.Model):
  title = models.CharField(max_length=255)
  abstract = models.CharField(max_length=255)
  file = models.FileField(upload_to='uploads/')
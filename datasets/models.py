from django.db import models
from dataType.models import DataType
from project.models import Project
from topic.models import Topic
from tag.models import Tag
from spatialInfo.models import SpatialRepresentationInfo
from boundingbox.models import boundingBox
from contact.models import Contact
#from anchor.models.fields import BlobField

class Dataset(models.Model):
  title = models.CharField(max_length=255)
  abstract = models.CharField(max_length=255)
  temporalCoverageFrom = models.DateTimeField()
  temportalCoverageTo	= models.DateTimeField()
  language = models.CharField(max_length=255,default='en') 	
  version	= models.CharField(max_length=255,default='1.0.0')
  openAccess = models.BooleanField()
  dataType = models.ForeignKey(DataType, on_delete=models.CASCADE, related_name='datatype_id')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_id')
  SpatialInfo = models.ForeignKey(SpatialRepresentationInfo, on_delete=models.CASCADE, related_name='SpatialRepresentationInfo_id')
  autoGenerateBBOX = models.BooleanField()
  boundingBox = models.ForeignKey(boundingBox, on_delete=models.CASCADE, related_name='boundingBox_id',null=True,blank=True)
  GeoReferenceSystem	= models.CharField(max_length=255,default='EPSG:4326')
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact_id')
  publisher	= models.CharField(max_length=255,default='Tuvalu Government')
  license	= models.CharField(max_length=255,default='Open Data Commons Open Database License (ODbL)')
  Tag = models.ManyToManyField(Tag, related_name='tags',blank=True)
  Topic = models.ManyToManyField(Topic, related_name='topics',blank=True)
  LocalAccessPath	= models.CharField(max_length=255,null=True,blank=True)
  file = models.FileField(upload_to='uploads/',null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True)  # Set when the object is created
  updated_at = models.DateTimeField(auto_now=True) 
  
  def __str__(self):
      return self.title
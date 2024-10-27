from django.contrib import admin
from .models import Dataset
# Register your models here.
class DatasetAdmin(admin.ModelAdmin):
    list_display = ("title","dataType","project","SpatialInfo",)

admin.site.register(Dataset,DatasetAdmin)
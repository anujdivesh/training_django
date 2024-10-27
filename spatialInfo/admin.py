from django.contrib import admin

# Register your models here.
from .models import SpatialRepresentationInfo

class SpatialRepresentationInfoAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(SpatialRepresentationInfo,SpatialRepresentationInfoAdmin)
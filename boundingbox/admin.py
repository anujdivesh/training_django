from django.contrib import admin

# Register your models here.
from .models import boundingBox

class boundingBoxAdmin(admin.ModelAdmin):
    list_display = ("island_name",)

admin.site.register(boundingBox,boundingBoxAdmin)
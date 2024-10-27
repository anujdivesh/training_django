from django.contrib import admin

# Register your models here.
from .models import DataType

class DataTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(DataType,DataTypeAdmin)
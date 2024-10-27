from django.urls import path,include
from . import views
from .views import DataTypeView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'datatype', DataTypeView)


urlpatterns = [
    path('', include(router.urls)),
]

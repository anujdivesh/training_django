from django.urls import path,include
from . import views
from .views import SpatialRepresentationInfoView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'spatialinfo', SpatialRepresentationInfoView)


urlpatterns = [
    path('', include(router.urls)),
]

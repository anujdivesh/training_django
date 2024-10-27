from django.urls import path,include
from . import views
from .views import boundingBoxView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bbox', boundingBoxView)


urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path,include
from . import views
from .views import TagView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tag', TagView)


urlpatterns = [
    path('', include(router.urls)),
]

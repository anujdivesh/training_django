from django.urls import path,include
from . import views
from .views import TopicView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'topic', TopicView)


urlpatterns = [
    path('', include(router.urls)),
]

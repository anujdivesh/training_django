from django.urls import path,include
from . import views
from .views import ContactView  
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contact', ContactView)


urlpatterns = [
    path('', include(router.urls)),
]

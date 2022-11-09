from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import HorarioViewSet


routers = SimpleRouter()

routers.register('', HorarioViewSet, basename='horarios')

urlpatterns = [
    path('', include(routers.urls), name='horarios'),
]
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import DisponibilidadeViewSet


routers = SimpleRouter()

routers.register(r'', DisponibilidadeViewSet, basename='disponibilidades')

urlpatterns = [
    path('', include(routers.urls), name='disponibilidades'),
]
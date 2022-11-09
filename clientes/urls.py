from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ClienteViewSet


routers = SimpleRouter()

routers.register(r'', ClienteViewSet, basename='clientes')

urlpatterns = [
    path('', include(routers.urls), name='clientes'),
]
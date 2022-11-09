from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ConfiguracaoViewSet


routers = SimpleRouter()

routers.register(r'', ConfiguracaoViewSet, basename='configuracoes')

urlpatterns = [
    path('', include(routers.urls), name='configuracoes'),
]
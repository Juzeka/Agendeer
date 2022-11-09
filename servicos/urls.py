from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ServicoViewSet


routers = SimpleRouter()

routers.register(r'', ServicoViewSet, basename='servicos')

urlpatterns = [
    path('', include(routers.urls), name='servicos'),
]
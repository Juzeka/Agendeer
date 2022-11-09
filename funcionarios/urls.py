from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FuncionarioViewSet


routers = SimpleRouter()

routers.register(r'', FuncionarioViewSet, basename='funcionarios')

urlpatterns = [
    path('', include(routers.urls), name='funcionarios'),
]
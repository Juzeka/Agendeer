from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AgendamentoViewSet


routers = SimpleRouter()

routers.register(r'', AgendamentoViewSet, basename='agendamentos')

urlpatterns = [
    path('', include(routers.urls), name='agendamentos'),
]
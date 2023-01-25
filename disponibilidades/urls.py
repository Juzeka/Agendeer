from django.urls import path
from .views import DisponibilidadeViewSet


urlpatterns = [
    path(
        r'list',
        DisponibilidadeViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        r'create',
        DisponibilidadeViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        r'update/<int:pk>',
        DisponibilidadeViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        r'detail/<int:pk>',
        DisponibilidadeViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        r'delete/<int:pk>',
        DisponibilidadeViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

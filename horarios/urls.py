from django.urls import path
from .views import HorarioViewSet


urlpatterns = [
    path(
        'list',
        HorarioViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'create',
        HorarioViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'update/<int:pk>',
        HorarioViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'detail/<int:pk>',
        HorarioViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'delete/<int:pk>',
        HorarioViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

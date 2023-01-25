from django.urls import path
from .views import FuncionarioViewSet


urlpatterns = [
    path(
        'list',
        FuncionarioViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'create',
        FuncionarioViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'update/<int:pk>',
        FuncionarioViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'detail/<int:pk>',
        FuncionarioViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'get_schedulings_today',
        FuncionarioViewSet.as_view(actions={'get': 'get_schedulings_today'}),
        name='get_schedulings_today'
    ),
    path(
        'get_schedulings_all',
        FuncionarioViewSet.as_view(actions={'get': 'get_schedulings_all'}),
        name='get_schedulings_all'
    ),
    path(
        'get_schedules_available_date',
        FuncionarioViewSet.as_view(actions={'get': 'get_schedules_available_date'}),
        name='get_schedules_available_date'
    ),
]

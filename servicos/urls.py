from django.urls import path
from .views import ServicoViewSet


urlpatterns = [
    path(
        'list',
        ServicoViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'create',
        ServicoViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'update/<int:pk>',
        ServicoViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'detail/<int:pk>',
        ServicoViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'delete/<int:pk>',
        ServicoViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

from django.urls import path
from .views import ConfiguracaoViewSet


urlpatterns = [
    path(
        r'list',
        ConfiguracaoViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        r'create',
        ConfiguracaoViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        r'update/<int:pk>',
        ConfiguracaoViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        r'detail/<int:pk>',
        ConfiguracaoViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        r'delete/<int:pk>',
        ConfiguracaoViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

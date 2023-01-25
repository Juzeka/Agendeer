from django.urls import path
from .views import ClienteViewSet


urlpatterns = [
    path(
        'list',
        ClienteViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'create',
        ClienteViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'update/<int:pk>',
        ClienteViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'detail/<int:pk>',
        ClienteViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'delete/<int:pk>',
        ClienteViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

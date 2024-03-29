from django.urls import path
from .views import AgendamentoViewSet


urlpatterns = [
    path(
        'list',
        AgendamentoViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'create/',
        AgendamentoViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'update/<int:pk>',
        AgendamentoViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'detail/<int:pk>',
        AgendamentoViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'delete/<int:pk>',
        AgendamentoViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
    path(
        'cancel/user/<str:protocolo>/',
        AgendamentoViewSet.as_view(actions={'get': 'cancel_user'}),
        name='cancel_user'
    ),
    path(
        'cancel/<int:pk>/',
        AgendamentoViewSet.as_view(actions={'get': 'cancel'}),
        name='cancel'
    ),
    path(
        'finish/<int:pk>/',
        AgendamentoViewSet.as_view(actions={'get': 'finish'}),
        name='finish'
    ),
]

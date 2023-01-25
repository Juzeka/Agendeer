from django.urls import path
from .views import (
    ContentTypeViewSet,
    UserViewSet,
    PermissionViewSet,
    GroupViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]

urlpatterns += [
    path(
        'apps/list',
        ContentTypeViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'apps/create',
        ContentTypeViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'apps/update/<int:pk>',
        ContentTypeViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'apps/detail/<int:pk>',
        ContentTypeViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'apps/delete/<int:pk>',
        ContentTypeViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

urlpatterns += [
    path(
        'user/list',
        UserViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'user/create',
        UserViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'user/update/<int:pk>',
        UserViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'user/detail/<int:pk>',
        UserViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'user/delete/<int:pk>',
        UserViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
    path(
        'user/create_user_simple',
        UserViewSet.as_view(actions={'post': 'simple_create'}),
        name='create_user_simple'
    ),
]

urlpatterns += [
    path(
        'permissions/list',
        PermissionViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'permissions/create',
        PermissionViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'permissions/update/<int:pk>',
        PermissionViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'permissions/detail/<int:pk>',
        PermissionViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'permissions/delete/<int:pk>',
        PermissionViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

urlpatterns += [
    path(
        'groups/list',
        GroupViewSet.as_view(actions={'get': 'list'}),
        name='list'
    ),
    path(
        'groups/create',
        GroupViewSet.as_view(actions={'post': 'create'}),
        name='create'
    ),
    path(
        'groups/update/<int:pk>',
        GroupViewSet.as_view(actions={'put': 'update'}),
        name='update'
    ),
    path(
        'groups/detail/<int:pk>',
        GroupViewSet.as_view(actions={'get': 'retrieve'}),
        name='detail'
    ),
    path(
        'groups/delete/<int:pk>',
        GroupViewSet.as_view(actions={'delete': 'destroy'}),
        name='destroy'
    ),
]

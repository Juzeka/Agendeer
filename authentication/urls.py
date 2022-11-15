from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserViewSet,
    PermissionViewSet,
    GroupViewSet,
    ContentTypeViewSet
)


routers = SimpleRouter()

routers.register(r'users', UserViewSet, basename='users')
routers.register(r'permissions', PermissionViewSet, basename='permissions')
routers.register(r'groups', GroupViewSet, basename='groups')
routers.register(r'apps', ContentTypeViewSet, basename='apps')

urlpatterns = [
    path('', include(routers.urls), name='users'),
]
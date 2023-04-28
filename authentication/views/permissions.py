from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    Permission, PermissionSerializerAll,
)


class PermissionViewSet(ModelViewSet):
    serializer_class = PermissionSerializerAll
    queryset = Permission.objects.all()

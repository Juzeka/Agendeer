from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    Permission, PermissionSerializerAll,
)

# manter temporariamente livre
class PermissionViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = PermissionSerializerAll
    queryset = Permission.objects.all()

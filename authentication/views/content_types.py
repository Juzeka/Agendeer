from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    ContentType, ContentTypeSerializerAll
)

# manter temporariamente livre
class ContentTypeViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = ContentTypeSerializerAll
    queryset = ContentType.objects.all()

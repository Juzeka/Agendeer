from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    ContentType, ContentTypeSerializerAll
)


class ContentTypeViewSet(ModelViewSet):
    serializer_class = ContentTypeSerializerAll
    queryset = ContentType.objects.all()

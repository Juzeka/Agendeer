from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from ..serializers import ClienteSerializerAll
from ..models import Cliente


class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializerAll
    queryset = Cliente.objects.all()

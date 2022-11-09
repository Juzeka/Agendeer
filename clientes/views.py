from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from .serializers import ClienteSerializerAll
from .models import Cliente


class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializerAll
    queryset = Cliente.objects.all()

    @action(methods=['get'], detail=False)
    def teste(self, request):
        return Response(data={'chave':'retorna uma lista'}, status=HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def teste1(self, request, pk=None):
        return Response(data={'chave':pk}, status=HTTP_200_OK)


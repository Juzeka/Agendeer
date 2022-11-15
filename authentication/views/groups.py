from rest_framework.decorators import action
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from ..serializers import (
    Group, GroupSerializerAll,
)
from ..services import GroupService
from configuracoes.models import Configuracao


# manter temporariamente livre
class GroupViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = GroupSerializerAll
    queryset = Group.objects.all()
    service_class = GroupService

    @action(methods=['get'], detail=False)
    def criar_grupos_padroes(self, request):
        msg = 'Os grupos já foram criados!'

        if not Configuracao.objects.first().grupos_permissao:
            msg = 'Grupos criados com sucesso!'
            self.service_class().criar_grupos_padroes()

        return Response(msg, status=HTTP_200_OK)

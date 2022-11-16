from rest_framework.viewsets import ModelViewSet
from ..serializers import ServicoSerializerAll
from ..models import Servico


class ServicoViewSet(ModelViewSet):
    serializer_class = ServicoSerializerAll
    queryset = Servico.objects.all()

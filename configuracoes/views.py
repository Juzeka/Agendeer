from rest_framework.viewsets import ModelViewSet
from .serializers import ConfiguracaoSerializerAll
from .models import Configuracao


class ConfiguracaoViewSet(ModelViewSet):
    serializer_class = ConfiguracaoSerializerAll
    queryset = Configuracao.objects.all()

from rest_framework.viewsets import ModelViewSet
from ..serializers import DisponibilidadeSerializerAll
from ..models import Disponibilidade


class DisponibilidadeViewSet(ModelViewSet):
    serializer_class = DisponibilidadeSerializerAll
    queryset = Disponibilidade.objects.all()

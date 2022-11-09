from rest_framework.viewsets import ModelViewSet
from .serializers import HorarioSerializerAll
from .models import Horario


class HorarioViewSet(ModelViewSet):
    serializer_class = HorarioSerializerAll
    queryset = Horario.objects.all()
from factory.django import DjangoModelFactory
from .models import Horario


class HorarioFactory(DjangoModelFactory):
    class Meta:
        model = Horario

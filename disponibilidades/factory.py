from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Disponibilidade


class DisponibilidadeFactory(DjangoModelFactory):
    class Meta:
        model = Disponibilidade

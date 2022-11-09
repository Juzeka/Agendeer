from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Configuracao


class ConfiguracaoFactory(DjangoModelFactory):
    class Meta:
        model = Configuracao
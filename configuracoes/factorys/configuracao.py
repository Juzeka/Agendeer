from factory.django import DjangoModelFactory
from factory import Sequence
from ..models.configuracao import Configuracao


class ConfiguracaoFactory(DjangoModelFactory):
    class Meta:
        model = Configuracao

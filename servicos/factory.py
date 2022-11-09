from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Servico
from decimal import Decimal
import random

class ServicoFactory(DjangoModelFactory):
    class Meta:
        model = Servico

    descricao = Sequence(lambda n: 'Descrição de Serviço %d' % n)
    valor = Decimal(random.uniform(10,30)).quantize(Decimal('.01'))
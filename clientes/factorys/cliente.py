from factory.django import DjangoModelFactory
from factory import Sequence
from ..models import Cliente
import random


class ClienteFactory(DjangoModelFactory):
    class Meta:
        model = Cliente

    nome_full = Sequence(lambda n: 'Fulando de Tal %d' % n)
    whatsapp = str(random.randint(10000000000, 99999999999))

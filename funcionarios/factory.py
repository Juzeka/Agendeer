from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Funcionario


class FuncionarioFactory(DjangoModelFactory):
    class Meta:
        model = Funcionario

    nome_full = Sequence(lambda n: 'Funcionario Fulando de Tal %d' % n)
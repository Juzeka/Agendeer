from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from ..models import Funcionario
from authentication.factorys import UserFactory


class FuncionarioFactory(DjangoModelFactory):
    class Meta:
        model = Funcionario

    user = SubFactory(UserFactory)
    nome_full = Sequence(lambda n: 'Funcionario Fulando de Tal %d' % n)

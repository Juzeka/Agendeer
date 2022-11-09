from factory.django import DjangoModelFactory
from factory import SubFactory
from .models import Agendamento
from clientes.factory import ClienteFactory
from funcionarios.factory import FuncionarioFactory
from servicos.factory import ServicoFactory


class AgendamentoFactory(DjangoModelFactory):
    class Meta:
        model = Agendamento

    cliente = SubFactory(ClienteFactory)
    funcionario = SubFactory(FuncionarioFactory)
    servico = SubFactory(ServicoFactory)
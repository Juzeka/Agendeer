from factory.django import DjangoModelFactory
from factory import SubFactory
from ..models import Agendamento
from clientes.factorys import ClienteFactory
from funcionarios.factorys import FuncionarioFactory
from servicos.factorys import ServicoFactory


class AgendamentoFactory(DjangoModelFactory):
    class Meta:
        model = Agendamento

    cliente = SubFactory(ClienteFactory)
    funcionario = SubFactory(FuncionarioFactory)
    servico = SubFactory(ServicoFactory)

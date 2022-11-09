from django.test import TestCase
from agendamentos.models import Agendamento
from disponibilidades.models import Disponibilidade
from agendamentos.factory import AgendamentoFactory
from agendamentos.services import AgendamentoService
from funcionarios.factory import FuncionarioFactory
from disponibilidades.factory import DisponibilidadeFactory
from horarios.factory import HorarioFactory
from parameterized import parameterized


class AgendamentoServiceTestCase(TestCase):
    model_class = Agendamento
    service_class = AgendamentoService

    def setUp(self):
        self.disponibilidade = DisponibilidadeFactory(data='2022-11-05')
        self.disponibilidade.horarios.add(
            HorarioFactory(horario='14:00'),
            HorarioFactory(horario='14:30')
        )

        self.funcionario1 = FuncionarioFactory()
        self.funcionario1.disponibilidades.add(self.disponibilidade)

    def test_desativar_horario_data_funcionario(self):
        agendamento = AgendamentoFactory(
            funcionario=self.funcionario1,
            data='2022-11-05',
            horario='14:30'
        )

        self.service_class(
            data=agendamento.data,
            horario=agendamento.horario,
            funcionario=self.funcionario1.pk
        ).desativar_horario_data_funcionario()

        disponibilidade = Disponibilidade.objects.filter(
            data=agendamento.data
        ).first()

        horario = disponibilidade.horarios.filter(
            horario=agendamento.horario
        ).first()

        self.assertFalse(horario.ativo)

    def test_ativar_horario_data_funcionario(self):
        agendamento = AgendamentoFactory(
            funcionario=self.funcionario1,
            data='2022-11-05',
            horario='14:00'
        )

        self.service_class(
            data=agendamento.data,
            horario=agendamento.horario,
            funcionario=agendamento.funcionario.pk
        ).ativar_horario_data_funcionario()

        disponibilidade = Disponibilidade.objects.filter(
            data=agendamento.data
        ).first()

        horario = disponibilidade.horarios.filter(
            horario=agendamento.horario
        ).first()

        self.assertTrue(horario.ativo)
from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from agendamentos.factory import AgendamentoFactory
from funcionarios.factory import FuncionarioFactory
from disponibilidades.factory import DisponibilidadeFactory
from horarios.factory import HorarioFactory
from clientes.factory import ClienteFactory
from servicos.factory import ServicoFactory
from agendamentos.models import Agendamento


class AgendamentoViewSetTestCase(TestCase):
    models_class = Agendamento

    def setUp(self):
        self.cliente1 = ClienteFactory()
        self.disponibilidade = DisponibilidadeFactory(data='2022-11-05')
        self.disponibilidade.horarios.add(
            HorarioFactory(horario='14:00'),
            HorarioFactory(horario='14:30')
        )

        self.funcionario1 = FuncionarioFactory()
        self.funcionario1.disponibilidades.add(self.disponibilidade)

        self.servico1 = ServicoFactory()
        self.agendamento1 = AgendamentoFactory(
            cliente=self.cliente1,
            funcionario=self.funcionario1,
            data='2022-11-05',
            horario='14:30'
        )
        self.agendamento2 = AgendamentoFactory(
            cliente=self.cliente1,
            funcionario=self.funcionario1,
            data='2022-11-05',
            horario='14:00'
        )

    def test_criar_agendamento(self):
        data = {
            "cliente": self.cliente1.pk,
            "funcionario": self.funcionario1.pk,
            "servico": self.servico1.pk,
            "data": "2022-11-05",
            "horario": "14:00",
        }

        response = self.client.post(
            '/v1/agendamentos/',
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_cancelar(self):
        response = self.client.get(
            f'/v1/agendamentos/{self.agendamento1.pk}/cancelar/'
        )

        instance = self.models_class.objects.filter(
            pk=self.agendamento1.pk
        ).first()

        horario = instance.funcionario.disponibilidades.filter(
            data=instance.data
        ).first().horarios.filter(horario=instance.horario).first()

        expected_result = {
            'mensage': 'Agendamento cancelado com sucesso!'
        }

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(expected_result, response.data)
        self.assertTrue(instance.cancelado)
        self.assertFalse(instance.ativo)
        self.assertTrue(horario.ativo)

    def test_concluir(self):
        response = self.client.get(
            f'/v1/agendamentos/{self.agendamento2.pk}/concluir/'
        )

        instance = self.models_class.objects.filter(
            pk=self.agendamento2.pk
        ).first()

        expected_result = {
            'mensage': 'Agendamento concluido com sucesso!'
        }

        self.assertEqual(expected_result, response.data)
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertFalse(instance.ativo)
        self.assertFalse(instance.cancelado)
        self.assertTrue(instance.concluido)


from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from agendamentos.factorys import AgendamentoFactory
from funcionarios.factorys import FuncionarioFactory
from disponibilidades.factorys.disponibilidade import DisponibilidadeFactory
from horarios.factorys import HorarioFactory
from clientes.factorys import ClienteFactory
from servicos.factorys import ServicoFactory
from agendamentos.models import Agendamento
from agendamentos.services import AgendamentoService
from django.contrib.auth.models import User


DATE_05_11_2022 = '2022-11-05'
HORARIO_14_00 = '14:00'
HORARIO_14_30 = '14:30'
HORARIO_15_00 = '15:00'


class AgendamentoViewSetTestCase(TestCase):
    models_class = Agendamento
    router_class = '/api/mgt/schedulings/'
    serivece_class = AgendamentoService

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='rafael',
            password='12345'
        )
        self.user.save()

        self.cliente1 = ClienteFactory()
        self.disponibilidade = DisponibilidadeFactory(data=DATE_05_11_2022)
        self.disponibilidade.horarios.add(
            HorarioFactory(horario=HORARIO_14_00, ativo=False),
            HorarioFactory(horario=HORARIO_14_30, ativo=False),
            HorarioFactory(horario=HORARIO_15_00, ativo=False)
        )

        self.funcionario1 = FuncionarioFactory(user=self.user)
        self.funcionario1.disponibilidades.add(self.disponibilidade)

        self.servico1 = ServicoFactory()
        self.agendamento1 = AgendamentoFactory(
            protocolo=AgendamentoService().get_protocolo(),
            cliente=self.cliente1,
            funcionario=self.funcionario1,
            data=DATE_05_11_2022,
            horario=HORARIO_14_30
        )
        self.agendamento2 = AgendamentoFactory(
            protocolo=AgendamentoService().get_protocolo(),
            cliente=self.cliente1,
            funcionario=self.funcionario1,
            data=DATE_05_11_2022,
            horario=HORARIO_14_00
        )

        self.data_token = self.client.post(
            '/api/auth/token/',
            data={
                'username': 'rafael',
                'password': '12345'
            }
        )
        self.headers = {
            'HTTP_AUTHORIZATION': f'Bearer {self.data_token.data.get("access")}'
        }

    def test_criar_agendamento_cliente_existente(self):
        data = {
            'cliente': self.cliente1.pk,
            'funcionario': self.funcionario1.pk,
            'servico': self.servico1.pk,
            'data': DATE_05_11_2022,
            'horario': HORARIO_14_00,
        }

        response = self.client.post(
            f'{self.router_class}create/',
            data=data,
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertTrue(response.data.get('protocolo'))

    def test_criar_agendamento_cliente_inexistente(self):
        data = {
            'nome_full': 'Rafael Gomes de Almeida',
            'whatsapp': '86998215671',
            'funcionario': self.funcionario1.pk,
            'servico': self.servico1.pk,
            'data': DATE_05_11_2022,
            'horario': HORARIO_14_00,
        }

        response = self.client.post(
            f'{self.router_class}create/',
            data=data,
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertTrue(response.data.get('protocolo'))

    def test_cancelar_via_protocolo(self):
        response = self.client.get(
            f'{self.router_class}cancel/user/{self.agendamento1.protocolo}/',
            **self.headers
        )

        expected_result = {'mensage': 'Agendamento cancelado com sucesso!'}

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(expected_result, response.data)

    def test_cancelar_via_pk(self):
        agendamento = AgendamentoFactory(
            protocolo=AgendamentoService().get_protocolo(),
            cliente=self.cliente1,
            funcionario=self.funcionario1,
            data=DATE_05_11_2022,
            horario=HORARIO_15_00
        )
        response = self.client.get(
            f'{self.router_class}cancel/{agendamento.pk}/',
            **self.headers
        )

        expected_result = {'mensage': 'Agendamento cancelado com sucesso!'}

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(expected_result, response.data)

    def test_concluir(self):
        response = self.client.get(
            f'{self.router_class}finish/{self.agendamento2.pk}/',
            **self.headers
        )

        expected_result = {'mensage': 'Agendamento finalizado!'}

        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(expected_result, response.data)

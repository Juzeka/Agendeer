from django.test import TestCase
from freezegun import freeze_time
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.models import User
from disponibilidades.factory import DisponibilidadeFactory
from horarios.factory import HorarioFactory
from funcionarios.factory import FuncionarioFactory
from agendamentos.factory import AgendamentoFactory
from clientes.factory import ClienteFactory
from datetime import date, time

DATE_15_11_2022 = date(year=2022, month=11, day=15)
DATE_16_11_2022 = date(year=2022, month=11, day=16)
HORARIO_10_00 = time(hour=10, minute= 0)
HORARIO_10_30 = time(hour=10, minute= 30)


class FuncionarioViewSetTestCase(TestCase):
    def setUp(self):
        self.horario1 = HorarioFactory(horario=HORARIO_10_00)
        self.horario2 = HorarioFactory(horario=HORARIO_10_30)

        self.disponibilidade1 = DisponibilidadeFactory(data=DATE_15_11_2022)
        self.disponibilidade1.horarios.add(self.horario1, self.horario2)

        self.user = User.objects.create(username='rafael')
        self.user.set_password('12345')
        self.user.save()

        self.funcionario1 = FuncionarioFactory(user=self.user)
        self.funcionario1.disponibilidades.add(self.disponibilidade1)

        self.agendamento1 = AgendamentoFactory(
            funcionario=self.funcionario1,
            data=DATE_15_11_2022,
            horario= HORARIO_10_00
        )
        self.agendamento2 = AgendamentoFactory(
            cliente=ClienteFactory(whatsapp='86998215671'),
            funcionario=self.funcionario1,
            data=DATE_16_11_2022,
            horario= HORARIO_10_30
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

    @freeze_time(DATE_15_11_2022)
    def test_get_schedulings_today(self):
        data_token = self.client.post(
            '/api/auth/token/',
            data={
                'username': 'rafael',
                'password': '12345'
            }
        )

        response = self.client.get(
            '/api/mgt/officials/get_schedulings_today/',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {data_token.data.get("access")}'
            }
        )

        expected_result = [
            {
                'ativo': self.agendamento1.ativo,
                'cancelado': self.agendamento1.cancelado,
                'cliente_id': self.agendamento1.cliente_id,
                'concluido': self.agendamento1.concluido,
                'data': self.agendamento1.data.strftime('%Y-%m-%d'),
                'funcionario_id': self.agendamento1.funcionario_id,
                'horario': self.agendamento1.horario.strftime('%H:%M:%S'),
                'id': self.agendamento1.pk,
                'servico_id': self.agendamento1.servico_id
            }
        ]

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json(), expected_result)

    def test_get_schedulings_all(self):
        data_token = self.client.post(
            '/api/auth/token/',
            data={
                'username': 'rafael',
                'password': '12345'
            }
        )

        response = self.client.get(
            '/api/mgt/officials/get_schedulings_all/',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {data_token.data.get("access")}'
            }
        )

        expected_result = [
            {
                'ativo': self.agendamento1.ativo,
                'cancelado': self.agendamento1.cancelado,
                'cliente_id': self.agendamento1.cliente_id,
                'concluido': self.agendamento1.concluido,
                'data': self.agendamento1.data.strftime('%Y-%m-%d'),
                'funcionario_id': self.agendamento1.funcionario_id,
                'horario': self.agendamento1.horario.strftime('%H:%M:%S'),
                'id': self.agendamento1.pk,
                'servico_id': self.agendamento1.servico_id
            },
            {
                'ativo': self.agendamento2.ativo,
                'cancelado': self.agendamento2.cancelado,
                'cliente_id': self.agendamento2.cliente_id,
                'concluido': self.agendamento2.concluido,
                'data': self.agendamento2.data.strftime('%Y-%m-%d'),
                'funcionario_id': self.agendamento2.funcionario_id,
                'horario': self.agendamento2.horario.strftime('%H:%M:%S'),
                'id': self.agendamento2.pk,
                'servico_id': self.agendamento2.servico_id
            }
        ]

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.json(), expected_result)

    def test_get_horarios_disponiveis_data(self):
        data = {
            'pk': self.funcionario1.pk,
            'data': DATE_15_11_2022
        }
        response = self.client.get(
            '/api/mgt/officials/get_schedules_available_date/',
            data=data,
            content_type='application/json',
            **self.headers
        )

        expected_result = [
            {
                'pk': self.horario1.pk,
                'horario': self.horario1.horario.strftime('%H:%M')
            },
            {
                'pk': self.horario2.pk,
                'horario': self.horario2.horario.strftime('%H:%M')
            }
        ]

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

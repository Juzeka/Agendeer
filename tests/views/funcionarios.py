from django.test import TestCase
from freezegun import freeze_time
from rest_framework.status import HTTP_201_CREATED
from django.contrib.auth.models import User
from disponibilidades.factorys.disponibilidade import DisponibilidadeFactory
from horarios.factorys import HorarioFactory
from funcionarios.factorys import FuncionarioFactory
from agendamentos.factorys import AgendamentoFactory
from clientes.factorys import ClienteFactory
from datetime import date, time
from authentication.services import GroupService
from agendamentos.services import AgendamentoService


DATE_15_11_2022 = date(year=2022, month=11, day=15)
DATE_16_11_2022 = date(year=2022, month=11, day=16)
HORARIO_10_00 = time(hour=10, minute= 0)
HORARIO_10_30 = time(hour=10, minute= 30)


class FuncionarioViewSetTestCase(TestCase):
    router_class = '/api/mgt/officials/'

    def setUp(self):
        self.grupos = GroupService().criar_grupos_padroes()
        self.horario1 = HorarioFactory(horario=HORARIO_10_00)
        self.horario2 = HorarioFactory(horario=HORARIO_10_30)

        self.disponibilidade1 = DisponibilidadeFactory(data=DATE_15_11_2022)
        self.disponibilidade1.horarios.add(self.horario1, self.horario2)

        self.user = User.objects.create_superuser(
            username='rafael',
            password='12345'
        )
        self.user.save()

        self.funcionario1 = FuncionarioFactory(user=self.user)
        self.funcionario1.disponibilidades.add(self.disponibilidade1)

        self.agendamento1 = AgendamentoFactory(
            protocolo=AgendamentoService().get_protocolo(),
            funcionario=self.funcionario1,
            data=DATE_15_11_2022,
            horario= HORARIO_10_00
        )
        self.agendamento2 = AgendamentoFactory(
            protocolo=AgendamentoService().get_protocolo(),
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

    def test_create(self):
        response = self.client.post(
            f'{self.router_class}create/',
            data={
                'username': 'funcionario_create',
                'password': 'funci',
                'groups': self.grupos[1].pk,
                'nome_full': 'Rafael Silva Labareda'
            },
            content_type='application/json',
            **self.headers
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(
            response.data.get('nome_full'),
            'Rafael Silva Labareda'
        )

from django.test import TestCase
from rest_framework.status import HTTP_200_OK
from disponibilidades.factory import DisponibilidadeFactory
from horarios.factory import HorarioFactory
from funcionarios.factory import FuncionarioFactory
from django.contrib.auth.models import User


DATE_15_11_2022 = '2022-11-15'


class FuncionarioViewSetTestCase(TestCase):
    def setUp(self):
        self.horario1 = HorarioFactory(horario='10:00')
        self.horario2 = HorarioFactory(horario='10:30')

        self.disponibilidade1 = DisponibilidadeFactory(data=DATE_15_11_2022)
        self.disponibilidade1.horarios.add(self.horario1, self.horario2)

        self.user = User.objects.create(username='rafael')
        self.user.set_password('12345')
        self.user.save()

        self.funcionario1 = FuncionarioFactory(user=self.user)
        self.funcionario1.disponibilidades.add(self.disponibilidade1)

        self.data_token = self.client.post(
            '/v1/auth/token/',
            data={
                'username': 'rafael',
                'password': '12345'
            }
        )

    def test_get_horarios_disponiveis_data(self):
        data = {
            'pk': self.funcionario1.pk,
            'data': DATE_15_11_2022
        }
        response = self.client.get(
            '/v1/funcionarios/get_horarios_disponiveis_data/',
            data=data,
            headers={'Authorization': f'Bearer {self.data_token.data.get("access")}'}
        )

        expected_result = [
            {
                'pk': self.horario1.pk,
                'horario': self.horario1.horario
            },
            {
                'pk': self.horario2.pk,
                'horario': self.horario2.horario
            }
        ]

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

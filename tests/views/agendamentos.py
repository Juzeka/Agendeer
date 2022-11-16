from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from agendamentos.factorys import AgendamentoFactory
from funcionarios.factorys import FuncionarioFactory
from disponibilidades.factorys.disponibilidade import DisponibilidadeFactory
from horarios.factorys import HorarioFactory
from clientes.factorys import ClienteFactory
from servicos.factorys import ServicoFactory
from agendamentos.models import Agendamento
from django.contrib.auth.models import User


DATE_05_11_2022 = '2022-11-05'
HORARIO_14_00 = '14:00'
HORARIO_14_30 = '14:30'


class AgendamentoViewSetTestCase(TestCase):
    models_class = Agendamento

    def setUp(self):
        self.user = User.objects.create(username='rafael')
        self.user.set_password('12345')
        self.user.save()

        self.cliente1 = ClienteFactory()
        self.disponibilidade = DisponibilidadeFactory(data=DATE_05_11_2022)
        self.disponibilidade.horarios.add(
            HorarioFactory(horario=HORARIO_14_00),
            HorarioFactory(horario=HORARIO_14_30)
        )

        self.funcionario1 = FuncionarioFactory(user=self.user)
        self.funcionario1.disponibilidades.add(self.disponibilidade)

        self.servico1 = ServicoFactory()
        self.agendamento1 = AgendamentoFactory(
            cliente=self.cliente1,
            funcionario=self.funcionario1,
            data=DATE_05_11_2022,
            horario=HORARIO_14_30
        )
        self.agendamento2 = AgendamentoFactory(
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
            '/api/schedulings/',
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)

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
            '/api/schedulings/',
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_cancelar(self):
        response = self.client.get(
            f'/api/schedulings/{self.agendamento1.pk}/cancelar/'
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
            f'/api/schedulings/{self.agendamento2.pk}/concluir/'
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


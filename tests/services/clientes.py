from django.test import TestCase
from clientes.services import ClienteService
from clientes.models import Cliente


class ClienteServiceTestCase(TestCase):
    service_class = ClienteService
    def setUp(self):
        ...

    def test_new_cliente_em_agendamento(self):
        expected_result = {
            'nome_full': 'Rafael Gomes de Almeida',
            'whatsapp': '86998215671'
        }

        response = self.service_class(
            **expected_result
        ).new_cliente_em_agendamento()

        self.assertIsInstance(response, Cliente)
        self.assertEqual(expected_result.get('nome_full'), response.nome_full)
        self.assertEqual(expected_result.get('whatsapp'), response.whatsapp)
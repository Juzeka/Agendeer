from django.test import TestCase
from funcionarios.factory import FuncionarioFactory
from funcionarios.services import FuncionarioService
from disponibilidades.factory import DisponibilidadeFactory
from horarios.factory import HorarioFactory


DATE_15_11_2022 = '2022-11-15'


class FuncionarioServiceTestCase(TestCase):
    service_class = FuncionarioService

    def setUp(self):
        self.horario1 = HorarioFactory(horario='10:00')
        self.horario2 = HorarioFactory(horario='10:30')

        self.disponibilidade1 = DisponibilidadeFactory(data=DATE_15_11_2022)
        self.disponibilidade1.horarios.add(self.horario1, self.horario2)

        self.funcionario1 = FuncionarioFactory()
        self.funcionario1.disponibilidades.add(self.disponibilidade1)

    def test_get_horarios_disponiveis_data(self):
        response = self.service_class(
            pk=self.funcionario1.pk,
            data=DATE_15_11_2022
        ).get_horarios_disponiveis_data()

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

        self.assertEqual(expected_result, response)
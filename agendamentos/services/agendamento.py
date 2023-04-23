import random
import string
from django.shortcuts import get_object_or_404
from funcionarios.models import Funcionario
from agendamentos.models import Agendamento
from horarios.serializers import HorarioSerializerAll
from agendamentos.serializers import AgendamentoSerializerAll
from utils.choices import CANCELADO


class AgendamentoService:
    model_class = Agendamento
    serializer_class = AgendamentoSerializerAll

    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data')
        self.horario = kwargs.get('horario')
        self.funcionario = kwargs.get('funcionario')
        self.status_horario = kwargs.get('status_horario')
        self.instance = kwargs.get('instance')

    def gerar_protocolo(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=4))
        numeros = ''.join(random.choices(string.digits, k=6))

        return f'{letras}{numeros}'

    def get_protocolo(self):
        protocolo = self.gerar_protocolo()

        while self.model_class.objects.filter(protocolo=protocolo).exists():
            protocolo = self.gerar_protocolo()

        return protocolo

    def alterar_status_horario_funcionario(self):
        funcionairo = get_object_or_404(Funcionario, pk=self.funcionario)
        disponibilidade = funcionairo.disponibilidades.filter(
            data=self.data,
            ativo=True
        )

        if disponibilidade.exists():
            disponibilidade = disponibilidade.first()
            horario = disponibilidade.horarios.filter(horario=self.horario)

            if horario.exists():
                horario = horario.first()

                serializer = HorarioSerializerAll(
                    instance=horario,
                    data={'ativo': self.status_horario},
                    partial=True
                )

                serializer.is_valid(raise_exception=True)
                serializer.save()

    def cancelar_agendamento(self):
        serializer = self.serializer_class(
            instance=self.instance,
            data={'status': CANCELADO},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.data = self.instance.data
        self.horario = self.instance.horario
        self.funcionario = self.instance.funcionario.pk
        self.status_horario = True

        self.alterar_status_horario_funcionario()

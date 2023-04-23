from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from ..serializers import (
    AgendamentoSerializerAll,
    AgendamentoSerializerResponseCreate
)
from ..models import Agendamento
from ..services import AgendamentoService
from clientes.models import Cliente
from clientes.services import ClienteService
from utils.choices import CONCLUIDO, ATIVO


class AgendamentoViewSet(ModelViewSet):
    serializer_class = AgendamentoSerializerAll
    model_class = Agendamento
    service_class = AgendamentoService

    def get_queryset(self):
        return self.model_class.objects.filter(status=ATIVO)

    def create(self, request, *args, **kwargs):
        cliente = Cliente.objects.filter(pk=request.data.get('cliente'))

        if not cliente.exists():
            data = request.data

            cliente = ClienteService(
                nome_full=data.get('nome_full'),
                whatsapp=data.get('whatsapp')
            ).new_cliente_em_agendamento()
        else:
            cliente = cliente.first()

        data_extra = {
            'cliente': cliente.pk,
            'protocolo': self.service_class().get_protocolo()
        }
        data = dict(data_extra, **request.data)

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        data = AgendamentoSerializerResponseCreate(serializer.instance).data

        return Response(data, status=HTTP_201_CREATED)

    def perform_create(self, serializer):
        super().perform_create(serializer)

        instance = serializer.instance

        self.service_class(
            data=instance.data,
            horario=instance.horario,
            funcionario=instance.funcionario.pk,
            status_horario=False
        ).alterar_status_horario_funcionario()

    def cancel_user(self, request, *args, **kwargs):
        agendamento = get_object_or_404(
            self.model_class,
            protocolo=kwargs.get('protocolo')
        )

        self.service_class(
            instance=agendamento
        ).cancelar_agendamento()

        return Response(
            data={
                'mensage': 'Agendamento cancelado com sucesso!'
            },
            status=HTTP_200_OK
        )

    def cancel(self, request, *args, **kwargs):
        agendamento = get_object_or_404(self.model_class, pk=kwargs.get('pk'))
        self.service_class(
            instance=agendamento
        ).cancelar_agendamento()

        return Response(
            data={
                'mensage': 'Agendamento cancelado com sucesso!'
            },
            status=HTTP_200_OK
        )

    def finish(self, request, *args, **kwargs):
        agendamento = get_object_or_404(self.model_class, pk=kwargs.get('pk'))

        serializer = self.serializer_class(
            agendamento,
            data={'status': CONCLUIDO, 'pago': True},
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response({'mensage': 'Agendamento finalizado!'})

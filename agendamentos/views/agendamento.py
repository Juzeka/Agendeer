from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from ..serializers import AgendamentoSerializerAll
from ..models import Agendamento
from ..services import AgendamentoService
from clientes.models import Cliente
from clientes.services import ClienteService
from clientes.serializers import ClienteSerializerAll


class AgendamentoViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = AgendamentoSerializerAll
    model_class = Agendamento

    def get_queryset(self):
        return self.model_class.objects.filter(ativo=True)

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

        data = request.data.copy()
        data.update({'cliente': cliente.pk})

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=HTTP_201_CREATED)

    def perform_create(self, serializer):
        super().perform_create(serializer)

        instance = serializer.instance

        AgendamentoService(
            data=instance.data,
            horario=instance.horario,
            funcionario=instance.funcionario.pk
        ).desativar_horario_data_funcionario()

    def set_cancel(self, agendamento):
        agendamento.cancelado = True
        agendamento.ativo = False

        AgendamentoService(
            data=agendamento.data,
            horario=agendamento.horario,
            funcionario=agendamento.funcionario.pk
        ).ativar_horario_data_funcionario()

        agendamento.save()

    @action(methods=['get'], detail=False)
    def cancel_user(self, request):
        try:
            cliente = Cliente.objects.filter(
                whatsapp=request.data.get('whatsapp')
            ).first()
            agendamento = get_object_or_404(
                self.model_class,
                cliente=cliente.pk
            )

            self.set_cancel(agendamento)

            return Response(
                data={
                    'mensage': 'Agendamento cancelado com sucesso!'
                },
                status=HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                data={
                    'mensage': 'Usúario incorreto ou não existe!'
                },
                status=HTTP_404_NOT_FOUND
            )

    @action(methods=['get'], detail=True, url_path='cancelar')
    def cancel(self, request, *args, **kwargs):
        agendamento = get_object_or_404(self.model_class, pk=kwargs.get('pk'))

        self.set_cancel(agendamento)

        return Response(
            data={
                'mensage': 'Agendamento cancelado com sucesso!'
            },
            status=HTTP_200_OK
        )

    @action(methods=['get'], detail=True, url_path='concluir')
    def finish(self, request, *args, **kwargs):
        agendamento = get_object_or_404(Agendamento, pk=kwargs.get('pk'))

        serializer = self.serializer_class(
            agendamento,
            data={'ativo': False, 'concluido': True},
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

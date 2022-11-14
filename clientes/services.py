from .serializers import ClienteSerializerAll


class ClienteService:
    serializer_class = ClienteSerializerAll

    def __init__(self, *args, **kwargs):
        self.nome_full = kwargs.get('nome_full')
        self.whatsapp = kwargs.get('whatsapp')

    def new_cliente_em_agendamento(self):
        serializer = self.serializer_class(
            data={
                'nome_full': self.nome_full,
                'whatsapp':self.whatsapp
            }
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return serializer.instance
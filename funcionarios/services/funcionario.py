from ..models import Funcionario
from horarios.serializers import HorarioSerializerAll


class FuncionarioService:
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.data = kwargs.get('data')

    def get_horarios_disponiveis_data(self):
        instance = Funcionario.objects.filter(pk=self.pk).first()
        disponibilidades = instance.disponibilidades.filter(
            data=self.data,
            ativo=True
        ).first()

        horarios = disponibilidades.horarios.filter(ativo=True)
        serializer = HorarioSerializerAll(horarios, many=True)

        return serializer.data

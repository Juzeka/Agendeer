from .models import Funcionario
class FuncionarioService:
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.data = kwargs.get('data')

    def get_horarios_disponiveis_data(self):
        instance = Funcionario.objects.filter(pk=self.pk).first()
        disponibilidades = instance.disponibilidades.filter(
            data=self.data
        ).first()

        horarios = disponibilidades.horarios.filter(ativo=True)

        data = [
            {
                'pk':obj.pk,
                'horario': obj.horario.strftime('%H:%M')
            } for obj in horarios
        ]

        return data

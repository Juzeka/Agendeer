from rest_framework import serializers
from ..models import Horario


class HorarioSerializerAll(serializers.ModelSerializer):
    horario = serializers.DateField(format='%H:%M')

    class Meta:
        model = Horario
        fields = '__all__'

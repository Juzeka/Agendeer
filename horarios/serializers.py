from rest_framework import serializers
from .models import Horario


class HorarioSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
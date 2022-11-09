from django.forms import ValidationError
from rest_framework import serializers
from .models import Cliente


class ClienteSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_whatsapp(self, value):
        if len(value) < 11:
            raise ValidationError('O número deve conter 11 digitos.')

        return value
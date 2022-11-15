from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 2


class CreateSimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'is_superuser', 'is_active',
            'is_staff', 'date_joined'
        ]

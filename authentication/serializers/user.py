from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime


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


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'is_active',
            'date_joined', 'groups'
        ]

    def validate(self, attrs):
        attrs.update({'date_joined': datetime.now(), 'is_active': True})

        return super().validate(attrs)

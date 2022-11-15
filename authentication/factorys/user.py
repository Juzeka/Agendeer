from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from factory import Sequence


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: 'username%d' % n)
    is_superuser = True
    is_staff = True
    is_active = True

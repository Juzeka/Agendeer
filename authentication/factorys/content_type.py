from factory.django import DjangoModelFactory
from django.contrib.contenttypes.models import ContentType
import random


NUM = random.randint(1,9)


class ContentTypeFactory(DjangoModelFactory):
    class Meta:
        model = ContentType

    app_label =f'{NUM}apps'
    model =f'{NUM}app'
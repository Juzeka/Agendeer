from django.db import models


class Cliente(models.Model):
    class Meta:
        unique_together = ['whatsapp']

    nome_full = models.CharField(max_length=200, blank=False, null=False)
    whatsapp = models.CharField(max_length=11, blank=False, null=False)
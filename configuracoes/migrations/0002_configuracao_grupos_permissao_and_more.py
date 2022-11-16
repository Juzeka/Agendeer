# Generated by Django 4.1.3 on 2022-11-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracao',
            name='grupos_permissao',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='Grupos de permissões padrão'),
        ),
        migrations.AlterField(
            model_name='configuracao',
            name='enviar_msg',
            field=models.BooleanField(auto_created=True, default=True, verbose_name='Enviar mensagens automaticas'),
        ),
    ]

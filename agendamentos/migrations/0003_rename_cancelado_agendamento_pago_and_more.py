# Generated by Django 4.1.3 on 2023-04-23 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_servico_titulo_alter_servico_ativo_and_more'),
        ('agendamentos', '0002_agendamento_protocolo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='cancelado',
            new_name='pago',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='concluido',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='status',
            field=models.CharField(choices=[('active', 'Ativo'), ('concluded', 'Concluído'), ('canceled', 'Cancelado')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='servico', to='servicos.servico'),
        ),
    ]
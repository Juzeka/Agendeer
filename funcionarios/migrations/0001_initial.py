# Generated by Django 4.1.3 on 2022-11-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disponibilidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_full', models.CharField(max_length=200)),
                ('disponibilidades', models.ManyToManyField(related_name='funcionario_disponibilidade', to='disponibilidades.disponibilidade')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-12 23:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appreservas', '0030_equipamento_nomeuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='agenda',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=30, verbose_name='Agendamento da Ferramenta - De:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='agenda_entrega',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=30, verbose_name='Agendamento da Ferramenta - Até:'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.1 on 2022-11-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreservas', '0020_alter_equipamento_agenda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='agenda_entrega',
            field=models.DateTimeField(max_length=30, verbose_name='Agendamento da Ferramenta - Até:'),
        ),
    ]

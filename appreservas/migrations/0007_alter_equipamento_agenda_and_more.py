# Generated by Django 4.0.1 on 2022-10-28 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreservas', '0006_alter_equipamento_agenda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='agenda',
            field=models.DateTimeField(max_length=30, verbose_name='Agendamento da Ferramenta - De:'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='agenda_entrega',
            field=models.DateTimeField(max_length=30, verbose_name='Agendamento da Ferramenta - Até:'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-10-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreservas', '0014_alter_equipamento_agenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='agenda',
            field=models.DateTimeField(max_length=30, verbose_name='Agendamento da Ferramenta - De:'),
        ),
    ]

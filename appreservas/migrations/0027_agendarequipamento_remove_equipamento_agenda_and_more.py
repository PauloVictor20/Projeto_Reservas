# Generated by Django 4.0.1 on 2022-12-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreservas', '0026_alter_equipamento_agenda_entrega'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendarEquipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome do Usuário:')),
                ('agenda', models.DateTimeField(max_length=30, verbose_name='Agendamento da Ferramenta - De:')),
                ('agenda_entrega', models.DateTimeField(max_length=30, verbose_name='Agendamento da Ferramenta - Até:')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipamento',
            name='agenda',
        ),
        migrations.RemoveField(
            model_name='equipamento',
            name='agenda_entrega',
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='nome',
            field=models.CharField(max_length=70, verbose_name='Nome da Ferramenta'),
        ),
    ]

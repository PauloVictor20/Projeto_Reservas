# Generated by Django 4.0.1 on 2022-10-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome')),
                ('identificacao', models.CharField(max_length=70, verbose_name='Código de Identificação')),
                ('uso', models.CharField(max_length=70, verbose_name='Tipo de Uso')),
            ],
        ),
    ]




from django.db import models

# Create your models here.


class Equipamento(models.Model):
    nome = models.CharField('Nome', max_length=70)
    idf = models.CharField('Código de Identificação', max_length=2)
    uso = models.CharField('Tipo de Uso', max_length=20)
    agenda = models.DateTimeField(
        'Agendamento da Ferramenta - De:', max_length=30, blank=True, null=True, unique=True  )
    agenda_entrega = models.DateTimeField(
        'Agendamento da Ferramenta - Até:', max_length=30, blank=True, null=True, unique=True )

    def __str__(self):
        return self.nome

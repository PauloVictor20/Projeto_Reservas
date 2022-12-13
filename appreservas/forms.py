from .models import Equipamento
from django import forms


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('nome', 'idf', 'uso', 'agenda', 'agenda entrega')

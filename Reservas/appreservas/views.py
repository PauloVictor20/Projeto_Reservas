
from django.shortcuts import render
from .models import Equipamento
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.


def home(request):
    return render(request, "home.html")


def pageopc(request):
    return render(request, "pageopc.html")


class EquipList(ListView):
    model = Equipamento
    template_name = 'equip_list.html'


class EquipCreate(CreateView):
    model = Equipamento
    template_name = 'equip_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('equip_list')
# def cadastroequip(request):
#    return render(request, "telacadastro.html")


class EquipUpdate(UpdateView):
    model = Equipamento
    template_name = 'equip_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('equip_list')


class EquipListAgenda(ListView):
    model = Equipamento
    template_name = 'equip_list_agenda.html'


class EquipDelete(DeleteView):
    model = Equipamento
    template_name = 'equip_confirm_delete.html'
    success_url = reverse_lazy('equip_list')


class EquipamentoDetail(DetailView):
    model = Equipamento
    template_name = 'equip_detail.html'


class EquipUpdateAgenda(UpdateView):
    model = Equipamento
    template_name = 'equip_create.html'
    fields = ['agenda', 'agenda_entrega']

    def get_success_url(self):
        return reverse('equip_list')

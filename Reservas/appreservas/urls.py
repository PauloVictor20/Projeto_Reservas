

from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home),
    path('opcitens', views.pageopc),
    path('equip_create', views.EquipCreate.as_view()),
    path('equip_list', views.EquipList.as_view(), name='equip_list'),
    path('equipamento/update/<int:pk>',
         views.EquipUpdate.as_view(), name='equip_update'),
    path('equipamento/delete/<int:pk>',
         views.EquipDelete.as_view(), name='equip_delete'),
    path('equipamento/details/<int:pk>',
         views.EquipamentoDetail.as_view(), name='equip_detail'),
    path('equip_list_agenda', views.EquipListAgenda.as_view(),
         name='equip_list_agenda'),
    path('equipamento/agendaupdate/<int:pk>',
         views.EquipUpdateAgenda.as_view(), name='equip_agenda_update'),

]

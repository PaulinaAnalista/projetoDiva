from django.urls import path
from . import views

urlpatterns = [
       
       path('', views.base, name='base'),
       path('servicos/', views.servico, name='servicos'),
       path('index/', views.index, name='index'),
       path('clientes/',views.clientes, name='clientes'),
       path('pagamentos/',views.pagamentos, name='pagamentos'),
       path('funcionarios/', views.funcionarios, name='funcionario'),
       path('agendamentos/', views.agendamentos, name='agendamentos'),

]

from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Servicos, Funcionarios, Pagamentos
from .forms import ClienteForm, ServicoForm, FuncionarioForm, PagamentoForm

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html') 
def clientes(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contacto = request.POST.get('contacto')

        Clientes.objects.create(nome=nome, email=email, contacto=contacto)
        return redirect('listar_clientes')  # ou outra página

    return render(request, 'clientes/clientes.html')


def servico(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')

        Servicos.objects.create(nome=nome, descricao=descricao, preco=preco)
        return redirect('listar_servicos')

    return render(request, 'clientes/servicos.html')





def funcionarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        data_contratacao = request.POST.get('data_contratacao')
        especializacao = request.POST.get('especializacao')

        Funcionarios.objects.create(
            nome=nome,
            telefone=telefone,
            data_contratacao=data_contratacao,
            especializacao=especializacao
        )
        return redirect('listar_funcionarios')

    return render(request, 'clientes/funcionarios.html')



def pagamentos(request):
    clientes = Clientes.objects.all()
    servicos = Servicos.objects.all()
    funcionarios = Funcionarios.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        servico_id = request.POST.get('servico')
        funcionario_id = request.POST.get('funcionario')
        valor_pago = request.POST.get('valor_pago')
        horario = request.POST.get('horario')
        status = request.POST.get('status')

        cliente = Clientes.objects.get(id=cliente_id)
        servico = Servicos.objects.get(id=servico_id)
        funcionario = Funcionarios.objects.get(id=funcionario_id) if funcionario_id else None

        Pagamentos.objects.create(
            cliente=cliente,
            servico=servico,
            funcionario=funcionario,
            valor_pago=valor_pago,
            horario=horario,
            status=status
        )
        return redirect('listar_pagamentos')

    return render(request, 'clientes/pagamentos.html', {
        'clientes': clientes,
        'servicos': servicos,
        'funcionarios': funcionarios
    })

def agendamentos(request):
    return render(request, 'clientes/agendamentos.html')









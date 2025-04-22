from django import forms
from .models import Clientes, Servicos, Funcionarios, Pagamentos

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
      

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = '__all__'
      

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = '__all__'

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamentos
        fields = '__all__'

from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    contacto = models.CharField(max_length=15, null=True, blank=True)

    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Servicos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    data_contratacao = models.DateField()
    especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pagamentos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL, null=True, blank=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateField(auto_now_add=True, null=True, blank=True)

    horario = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Pagamento de {self.valor_pago} por {self.clientes.nome}"


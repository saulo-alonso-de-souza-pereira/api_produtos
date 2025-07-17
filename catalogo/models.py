from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        COMUM = "COMUM", "Comum"
        ENTREGADOR = "ENTREGADOR", "Entregador"
    
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.COMUM)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Entrega(models.Model):
    class StatusEntrega(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        EM_ROTA = 'EM_ROTA', 'Em Rota'
        ENTREGUE = 'ENTREGUE', 'Entregue'
        CANCELADA = 'CANCELADA', 'Cancelada'
    
    destinatario = models.CharField(max_length=255)
    endereco = models.TextField()
    codigo_rastreio = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(
        max_length=10,
        choices=StatusEntrega.choices,
        default=StatusEntrega.PENDENTE
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, related_name="entregas")
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='entregas_como_cliente', default=CustomUser.Role.COMUM)
    entregador_atribuido = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='entregas_como_entregador')
    def __str__(self):
        return f"Entrega para {self.destinatario} - {self.status}"


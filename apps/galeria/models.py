from django.db import models

from datetime import datetime
# importo a tabela de usuario para criar o relacionamento entre a fotografia e o usuario que a criou

from django.contrib.auth.models import User

# Create your models here.
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=50, blank=False, null=False)
    legenda = models.CharField(max_length=150, blank=False, null=False)
    # Vou definir categorias especificas para evitar q o usuario crie categorias burramente
    # o parametro choices permite escolher dentre as opções de predefinidas
    # definir o default pra ele comecar a funcionar
    categoria = models.CharField(max_length=100, default='',choices=OPCOES_CATEGORIA)
    descricao = models.TextField(blank=False, null=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    # Criação do relacionamento com a tabela de usuarios
    usuario = models.ForeignKey(
        to=User,
        # caso o usuario ana seja deletado,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"


from django.contrib import admin
from apps.galeria.models import Fotografia

# Register your models here.
# Adiciona o controle desse model no painel de adm
class ListandoFotografias(admin.ModelAdmin):
    # Parametros que eu quero editar dentro do painel de administrador
    list_display = ("id", "nome", "legenda", "descricao", "publicada")
    # parametros que sao links que levam para a edição do arquivo no banco de dados
    list_display_links = ("id", "nome")
    # Adiciona um campo de busca no admim
    search_fields = ("nome", )
    list_filter = ("categoria", "usuario")
    # Paginção no admin
    list_per_page = 20
    # inserir o controle de publicação ja no display
    list_editable = ("publicada", )

admin.site.register(Fotografia, ListandoFotografias)



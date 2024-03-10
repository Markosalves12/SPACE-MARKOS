from django.urls import path
from apps.galeria.views import (index, imagem, buscar,
                                nova_imagem, editar_imagem,
                                deletar_imagem, filtro)

urlpatterns = [
    path('', index, name='index'),
    # 1 - navegando apenas numa pagina simples
    # path('imagem/', imagem, name='imagem')
    # 2 captura o id da foto pra renderizar a foto corretamente
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtros/<str:categoria>', filtro, name='filtro')
]
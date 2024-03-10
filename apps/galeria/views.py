from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# Para acessar o banco de dados é preciso importar o model
from apps.galeria.models import Fotografia

from django.contrib import messages


from apps.galeria.forms import FotografiaForms

def index(request):
    # o metodo HttpResponse retorna o
    # return HttpResponse('<h1>Alura space</h1><p>Bem vindo ao espaço</p>')

    # 1
    # Enviando dados dinamicamente para o html
    # dados = {
    #     1: {"nome": "Nebulosa de carina",
    #         "legenda": "webbtelescope.org / NASA /James webb"},
    #     2: {"nome": "galaxia NGC 1079",
    #         "legenda": "webbtelescope.org / NASA /Hubble"},
    # }

    # 2
    # assim conseguimos passar to o banco de dados de forma dinamica para a página de index
    # 3
    # fotografias = Fotografia.objects.all()
    # cado o usuario nao esteja logado e redirecionado por login
    if not request.user.is_authenticated:
        messages.error(request, "usuario nao logado")
        return redirect('login')


    #selecionar apenas as fotografias publicas
    # o sinal de menos controla a ordem da ordenação da mais antiga para a mais nova e vice versa
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    #O metodo render renderiza um arquivo html ja existente
    return render(request, 'galeria/index.html', {'cards': fotografias})

#Foto id passa o parametro para o url
def imagem(request, foto_id):
    # parametro pk = primary key
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    # Logica que prepara as fotos do banco de dados antes de ser enviada
    # cado o usuario nao esteja logado e redirecionado por login
    messages.error(request, "usuario nao logado")
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            # nome__icontains = o __icontains desliga a correpondencia exata e
            # permite busca com trechos de string
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "usuario nao logado")
        return redirect('login')

    form = FotografiaForms
    if request.method == 'POST':
        # Cadastra as informações e os arquivos
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia cadastrada")
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia Editada")
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso')

    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {'cards': fotografias})
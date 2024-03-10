from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForm

# Bibliotecxa do django para fazer autenticaç~eos na base de usuário
from django.contrib import auth

# tabela de usuarios que ja existe dentro do django para fazer a vericação se o usuario ja existe
from django.contrib.auth.models import User

# biblioteca django que printa mensagem para usuario
from django.contrib import messages
# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha,
        )
        if usuario is not None:
            auth.login(request, usuario)
            # messages.success(request, f"{nome} logado com sucesso")
            return redirect('index')
        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForm()
    # a requisição que manda pra url envia dados do formulario por isso o metodo post
    if request.method == 'POST':
        # eu quero que receba as infomações dentro de outro formulario
        form = CadastroForm(request.POST)

        if form.is_valid():
            # # Existe uma verificação a ser feita antes que é a senha
            # if form['senha_1'].value() != form['senha_2'].value():
            #     messages.error(request, "senha não são iguais")
            #     return redirect('cadastro')

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            #username = nome da coluna dentro da tabela user
            if User.objects.filter(username=nome).exists():
                messages.error(request, f"{nome} já existe")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save()
            messages.success(request, f"{nome} cadastrado com sucesso")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')
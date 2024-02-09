
from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Atividade
from .form import ProjetoForm, AtividadeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q, Count
from functools import reduce
from operator import or_


# Função Index
def index(request):
    usuario = request.user # Obtenha o usuário atual
    projetos = Projeto.objects.filter(usuario=usuario) # Filtra todos os projetos do usuário atual.
    # Obtenha a contagem de projetos por status
    status_counts = projetos.values('status').annotate(count=Count('id'))
    # Obtenha a contagem de projetos por área
    area_counts = projetos.values('area').annotate(count=Count('id'))
    # Converta os resultados para um formato que pode ser serializado para JSON
    status_counts_dict = {item['status']: item['count'] for item in status_counts}
    area_counts_dict = {item['area']: item['count'] for item in area_counts}
    # Retorne os resultados como JsonResponse
    return render(request, 'index.html', {'projetos': projetos, 'status_counts': status_counts_dict, 'area_counts': area_counts_dict})

# Função Login
def login_user(request):
    return render(request, 'login.html')

# Função Logout
def logout_user(request):
    logout(request)
    return redirect('/login/')

# Função Submit Login
def submit_login(request):
    if request.POST: # Condicional que verifica se o método da requisição é POST.
        username = request.POST.get('username') # Obtenha o valor do campo username do formulário.
        password = request.POST.get('password') # Obtenha o valor do campo password do formulário.
        print(username, password) 
        user = authenticate(username=username, password=password) # Autentica o usuário.
        if user is not None: # Condicional que verifica se o usuário é diferente de nulo.
            login(request, user) # Loga o usuário.
            return redirect('/index/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

# Função lista de projetos
@login_required(login_url='/login/')
def lista_projetos(request):
    usuario = request.user # Obtenha o usuário atual
    projetos = Projeto.objects.filter(usuario=usuario) # Filtra todos os projetos do usuário atual.
    return render(request, 'lista_projetos.html', {'projetos': projetos}) # Renderiza a página lista_projetos.html com a lista de projetos.

# Função cadastro de projetos
@login_required(login_url='/login/')
def cadastro_projetos(request):
    users = User.objects.all() # Obtenha todos os usuários do sistema.
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid(): # Condicional que verifica se o formulário é válido.
            novo_projeto = form.save(commit=False) # Salva o formulário.
            novo_projeto.usuario = request.user # Define o usuário do projeto como o usuário atual.
            novo_projeto.save() # Salva o projeto.
            return redirect('lista_projetos')
        else:
            print("Formulário não é válido. Erros:", form.errors)
    else:
        form = ProjetoForm(instance=Projeto()) # Cria uma instância do formulário ProjetoForm.
    return render(request, 'cadastro_projetos.html', {'form': form, 'users': users})

# Função delete projeto
@login_required(login_url='/login/')
def delete_projeto(request, id_projeto):
    usuario = request.user # Obtenha o usuário atual
    projeto = Projeto.objects.get(id=id_projeto) # Obtenha o projeto pelo id.
    if usuario == projeto.usuario: # Condicional que verifica se o usuário é o proprietário do projeto.
        projeto.delete() # Deleta o projeto.
    return redirect('lista_projetos')

# Função update projeto
@login_required(login_url='/login/')
def update_projeto(request, id_projeto): # Função update_projeto que recebe o id do projeto como parâmetro.
    projeto = Projeto.objects.get(id=id_projeto, usuario=request.user) # Obtenha o projeto pelo id e pelo usuário.
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto) # Cria uma instância do formulário ProjetoForm.
        if form.is_valid(): # Condicional que verifica se o formulário é válido.
            form.save() # Salva o formulário.
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto) # Cria uma instância do formulário ProjetoForm.

    return render(request, 'cadastro_projetos.html', {'form': form, 'projeto': projeto, 'user': request.user})

# Função cadastro de atividades
@login_required(login_url='/login/')
def cadastro_atividades(request):
    projetos = Projeto.objects.all()  # Obtenha todos os projetos do sistema.
    if request.method == 'POST':
        form = AtividadeForm(request.POST) # Cria uma instância do formulário AtividadeForm.
        if form.is_valid():
            nova_atividade = form.save(commit=False) # Salva o formulário.
            nova_atividade.usuario = request.user # Define o usuário da atividade como o usuário atual.
            nova_atividade.save() # Salva a atividade.
            return redirect('lista_atividades')
        else:
            print("Formulário não é válido. Erros:", form.errors) # Imprime os erros do formulário.
            return render(request, 'cadastro_atividades.html', {'form': form, 'projetos': projetos}) # Renderiza a página cadastro_atividades.html com o formulário e a lista de projetos.
    else:
        return render(request, 'cadastro_atividades.html', {'form': AtividadeForm(instance=Atividade()), 'projetos': projetos}) # Renderiza a página cadastro_atividades.html com o formulário e a lista de projetos.

# Função lista de atividades        
@login_required(login_url='/login/')
def lista_atividades(request):
    usuario = request.user # Obtenha o usuário atual
    atividades = Atividade.objects.filter(usuario=usuario) # Filtra todas as atividades do usuário atual.
    return render(request, 'lista_atividades.html', {'atividades': atividades}) # Renderiza a página lista_atividades.html com a lista de atividades.
       
# Função delete atividade
@login_required(login_url='/login/')
def delete_atividade(request, id_atividade): # Função delete_atividade que recebe o id da atividade como parâmetro.
    atividade = Atividade.objects.get(id=id_atividade) # Obtenha a atividade pelo id.
    atividade.delete() # Deleta a atividade.
    return redirect('lista_atividades')

# Função update atividade
@login_required(login_url='/login/')
def update_atividade(request, id_atividade): # Função update_atividade que recebe o id da atividade como parâmetro.
    atividade = get_object_or_404(Atividade, id=id_atividade, usuario=request.user) # Obtenha a atividade pelo id e pelo usuário.
    projetos = Projeto.objects.all() # Obtenha todos os projetos do sistema.
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade) # Cria uma instância do formulário AtividadeForm.
        if form.is_valid(): # Condicional que verifica se o formulário é válido.
            form.save() # Salva o formulário.
            return redirect('lista_atividades')
    else:
        form = AtividadeForm(instance=atividade) # Cria uma instância do formulário AtividadeForm.
    return render(request, 'cadastro_atividades.html', {'form': form, 'atividade': atividade, 'projetos': projetos, 'user': request.user}) # Renderiza a página cadastro_atividades.html com o formulário, a atividade, a lista de projetos e o usuário.

# Função pesquisa
@login_required(login_url='/login/')
def resultado_pesquisa(request):
    usuario = request.user # Obtenha o usuário atual
    pesquisa_query = request.GET.get('q', '') # Obtenha o valor do campo q da barra de pesquisa.
    if pesquisa_query:
        termos_pesquisa = pesquisa_query.split() # Separa os termos da pesquisa.
        condicoes_projetos = [Q(titulo__icontains=termo) | Q(proprietario__icontains=termo, usuario=usuario) for termo in termos_pesquisa] # Cria uma lista de condições para a pesquisa.
        resultados_projetos = Projeto.objects.filter(reduce(or_, condicoes_projetos)) # Filtra os projetos que atendem as condições da pesquisa.
        return render(request, 'resultado_pesquisa.html', {'resultados': resultados_projetos, 'pesquisa_query': pesquisa_query}) # Renderiza a página resultado_pesquisa.html com os resultados da pesquisa e a pesquisa_query.
    else:
        return render(request, 'resultado_pesquisa.html', {'mensagem': 'Por favor, insira algo na barra de pesquisa.'}) # Renderiza a página resultado_pesquisa.html com a mensagem de erro.

# Função detalhes do projeto
@login_required(login_url='/login/')
def detalhes_projeto(request, projeto_id): # Função detalhes_projeto que recebe o id do projeto como parâmetro.
    projeto = get_object_or_404(Projeto, pk=projeto_id, usuario=request.user) # Obtenha o projeto pelo id e pelo usuário.
    atividades = projeto.atividade_set.filter(usuario=request.user) # Obtenha todas as atividades do projeto.
    context = {'projeto': projeto, 'atividades': atividades} # Cria um dicionário com o projeto e as atividades.
    return render(request, 'detalhes_projeto.html', context) # Renderiza a página detalhes_projeto.html com o dicionário context.
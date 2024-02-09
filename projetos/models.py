from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

# Criação da tabela Projeto.
class Projeto(models.Model):
        id = models.AutoField(primary_key=True, verbose_name='ID')
        titulo = models.CharField(max_length=255, default='', verbose_name='Título')
        prioridade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0, verbose_name='Prioridade')
        acao_no_sprint = models.CharField(max_length=255, default='', verbose_name='Ação no Sprint')
        status_choices = [('Não Iniciado', 'Não Iniciado'), ('Em andamento', 'Em andamento'), ('Em Homologação', 'Em Homologação'), ('Parado', 'Parado'), ('Aguardando Terceiro', 'Aguardando Terceiro'), ('Cancelado', 'Cancelado'), ('Finalizado', 'Finalizado'),]
        status = models.CharField(max_length=255, choices=status_choices, default='', verbose_name='Status')
        area = models.CharField(max_length=255, default='', verbose_name='Área')
        tipo_de_projeto = models.CharField(max_length=255, default='', verbose_name='Tipo do Projeto')
        horas_estimadas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Horas Estimadas')
        data_inicio = models.DateField(default=timezone.now, verbose_name='Data de Início')
        prazo = models.DateField(default=timezone.now, verbose_name = 'Prazo de Conclusão')
        observacao = models.CharField(max_length=255, default='', verbose_name='Observação')
        proprietario = models.CharField(max_length=255, default='', verbose_name='Proprietário do Projeto')
        custo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Custo Estimado')
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

        def __str__(self):
            return self.titulo


# Criação da tabela Atividade.
class Atividade(models.Model):  
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nome = models.CharField(max_length=255, default='', verbose_name='Nome da Atividade')
    status_atividade_choices = [('Não Iniciado', 'Não Iniciado'), ('Em andamento', 'Em andamento'), ('Em Homologação', 'Em Homologação'), ('Parado', 'Parado'), ('Aguardando Terceiro', 'Aguardando Terceiro'), ('Cancelado', 'Cancelado'), ('Finalizado', 'Finalizado'),]
    status_atividade = models.CharField(max_length=255, choices=status_atividade_choices, default='', verbose_name='Status da Atividade')
    descricao = models.TextField(default='', verbose_name='Descrição da Atividade')
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, verbose_name='Projeto')
    horas_trabalhadas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Horas Trabalhadas')
    data_da_atividade = models.DateField(default=timezone.now, verbose_name='Data da Atividade')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    responsavel = models.CharField(max_length=255, default='', verbose_name='Responsável')

    def __str__(self):
        return self.nome


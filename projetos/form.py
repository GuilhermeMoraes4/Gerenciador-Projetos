from django import forms
from .models import Projeto, Atividade


# Classe ProjetoForm
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        exclude = ['usuario']
        fiels = '__all__'
        
    def __init__(self, *args, **kwargs):  # Função __init__ que herda de forms.ModelForm        
        super().__init__(*args, **kwargs) # Chamada do método __init__ da classe pai.
        for field_name, field in self.fields.items(): # Laço de repetição que percorre todos os campos do formulário.
            self.fields[field_name].widget.attrs.update({'class': 'form-control'}) # Adiciona a classe form-control a todos os campos do formulário.


# Classe AtividadeForm
class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        exclude = ['usuario']
        fields = ['nome', 'descricao', 'projeto', 'status_atividade', 'horas_trabalhadas', 'data_da_atividade', 'responsavel']

    def __init__(self, *args, **kwargs):  # Função __init__ que herda de forms.ModelForm
        super().__init__(*args, **kwargs) # Chamada do método __init__ da classe pai.
        for field_name, field in self.fields.items(): # Laço de repetição que percorre todos os campos do formulário.
            if not isinstance(field, forms.fields.ChoiceField): # Condicional que verifica se o campo não é do tipo ChoiceField.
                self.fields[field_name].widget.attrs.update({'class': 'form-control'}) # Adiciona a classe form-control a todos os campos do formulário.

    # Função save que herda de forms.ModelForm
    def save(self, commit=True): 
        atividade = super().save(commit=False) # Chamada do método save da classe pai.
        if commit: # Condicional que verifica se commit é verdadeiro.
            atividade.save() # Salva a atividade.
        return atividade # Retorna a atividade salva.

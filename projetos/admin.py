from django.contrib import admin
from .models import Projeto

# Registro do modelo Projeto no admin do Django.
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prazo', 'status', 'area')

admin.site.register(Projeto, ProjetoAdmin)


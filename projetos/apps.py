from django.apps import AppConfig

# Declaração da classe ProjetosConfig que herda de AppConfig.
class ProjetosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projetos'

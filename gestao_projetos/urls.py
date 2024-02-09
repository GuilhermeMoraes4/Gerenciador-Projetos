from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from projetos import views


# Caminhos de Urls criados para redirecionar para as views criadas o usuário do projeto.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro_projetos/', views.cadastro_projetos, name='cadastro_projetos'),
    path('index/', views.index , name='index'),
    path('', RedirectView.as_view(url='/login/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/delete/<int:id_projeto>/', views.delete_projeto, name='delete_projeto'),
    path('projetos/update/<int:id_projeto>/', views.update_projeto, name='update_projeto'),
    path('cadastro_atividades/', views.cadastro_atividades, name='cadastro_atividades'),
    path('atividades/', views.lista_atividades, name='lista_atividades'),
    path('atividades/delete/<int:id_atividade>/', views.delete_atividade, name='delete_atividade'), 
    path('atividades/update/<int:id_atividade>/', views.update_atividade, name='update_atividade'),  
    path('resultado_pesquisa/', views.resultado_pesquisa, name='resultado_pesquisa'),
    path('detalhes_projeto/<int:projeto_id>/', views.detalhes_projeto, name='detalhes_projeto'),

]


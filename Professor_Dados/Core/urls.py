from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('conteudos',views.Dados, name='conteudos'),
    path('login',views.Login, name='login'),
    path('cadastrar',views.Cadastrar, name='cadastrar'),
    path('dashbord', views.Dashbord, name='dashbord'),
    path('Criar_arquivo',views.Criar,name='Criar_arquivo'),
    path('Baixar',views.Baixar,name='Baixar'),
    path('sair',views.Sair, name='sair'),
    path('deletar/int:<id>',views.Deletar, name='deletar'),
]
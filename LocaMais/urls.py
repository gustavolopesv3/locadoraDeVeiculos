"""LocaMais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from locadora.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrocliente', cadastrocliente, name='cadastrocliente'),
    path('carros_cliente/<int:id>', listaveic_cliente, name='carros_cliente'),
    path('cadastroveiculo', cadastroveiculo, name='cadastroveiculo' ),
    path('editarveiculo/<int:id>', editarveiculo, name='editarveiculo' ),
    path('deletarveiculo/<int:id>', deletarveiculo, name='deletarveiculo' ),
    path('editarcliente/<int:id>', editarcliente, name='editarcliente' ),
    path('alguel', alguel, name='alguel'),
    path('receberalguel/<int:id>', receberalguel, name='receberalguel'),
    path('listclientes', listclientes, name='listclientes' ),
    path('cadastromarca', cadastromarca, name='cadastromarca' ),
    path('cadastromodelo', cadastromodelo, name='cadastromodelo' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', contaclientes, name='index'),
    path('listaraluguel', listaralguel, name='listaraluguel'),
    path('listaraluguel_finalizado', listaralguel_finalizado, name='listaraluguel_finalizado'),
    path('listarveiculos', listarveiculos, name='listarveiculos'),
    path('cadastro_usuario', cadastrar_usuario, name='cadastro_usuario'),
    path('listar_usuarios', listar_ususario, name='listar_usuarios'),
    path('teste', teste, name='teste'),
    path('todos_veiculos', todos_carros, name='todos_veiculos'),
]

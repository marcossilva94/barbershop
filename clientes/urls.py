from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_clientes/', views.cadastro_clientes, name="cadastro_clientes"),
    path('listar_clientes/', views.listar_clientes, name="listar_clientes")
]

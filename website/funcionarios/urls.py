from django.urls import path

# Importamos as funções e classes definidas no arquivo views.py
# from website.funcionarios.views import home, lista_funcionarios

from website.funcionarios.views import (
    HomeTemplateView,
    FuncionarioListView,
    FuncionarioCreateView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)

app_name = 'funcionarios'

# urlpatterns contém a lista de roteamentos de URLs

urlpatterns = [

    # GET /
    # path('', home, name='home'), <-- Exemplo com Função

    # GET /funcionarios
    # path('lista-funcionarios/', lista-funcionarios,
    #      name='lista-funcionarios'), <-- Exemplo com Função

    # GET /
    path('', HomeTemplateView.as_view(), name="home"),

    # POST /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(),
         name="cadastra-funcionario"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista-funcionarios"),

    # GET/POST /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(),
         name="atualiza-funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionario/excluir/<pk>',
         FuncionarioDeleteView.as_view(), name="deleta-funcionario"),
]

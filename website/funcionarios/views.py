from django.urls import reverse_lazy
from website.funcionarios.models import Funcionario
from website.funcionarios.forms import InsereFuncionarioForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView


# FBV - FUNCTION BASE VIEW
# ----------------------------------------------
# def home(request):
#     # Função
#     return HttpResponse("Olá Mundo")


# def lista_funcionarios(request):
#     """
#     Utilizando funções, você basicamente vai definir uma função que:
#    Recebe como parâmetro uma requisição ( request ).
#    Realiza algum processamento.
#    Retorna alguma informação.
#     """

#     # Primeiro buscamos os funcionarios
#     funcionarios = Funcionario.objetos.all()

#     # Incluímos no contexto
#     contexto = {
#         'funcionarios': funcionarios
#     }

#     # Retornamos o template para listar os funcionarios
#     return render(
#         request,
#         "funcionarios.html",
#         contexto
#     )


# def criar_funcionarios(request, pk):
#     # Verificamos se o método é POST
#     if request.method == 'POST':
#         form = FormularioDeCriacao(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('lista_funcionarios'))

#     # Qualquer outro método: GET, OPTION, DELETE, etc...
#     else:
#         return render(request, "templates/form.html", {'form': form})


# CBV - CLASSE BASE VIEW
# ----------------------------------------------

# PÁGINA PRINCIPAL
# ----------------------------------------------


class HomeTemplateView(TemplateView):
    template_name = "funcionarios/home.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------


class FuncionarioListView(ListView):
    """
    Já as Class Based Views são classes que herdam da classe do Django
    django.view.generic.base.View e que agrupam diversas
    funcionalidades e facilitam a vida do desenvolvedor.
    """
    template_name = "funcionarios/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------


class FuncionarioCreateView(CreateView):
    template_name = "funcionarios/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("funcionarios:lista-funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------


class FuncionarioUpdateView(UpdateView):
    template_name = "funcionarios/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("funcionarios:lista-funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------


class FuncionarioDeleteView(DeleteView):
    template_name = "funcionarios/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("funcionarios:lista-funcionarios")

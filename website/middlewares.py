from django.http.response import HttpResponseForbidden


"""
Um middleware é um método callable (que tem uma implementação
do método __call__() ) que recebe uma requisição e retorna uma
resposta e, assim como uma View, pode ser escrito como função ou
como Classe.


# Um exemplo de middleware escrito como função é:


def middleware_simples(get_response):

    # Código de inicialização do Middleware

    def middleware(request):
        # Código a ser executado antes da View e
        # antes de outros middlewares serem executados

        response = get_response(request)

    # Código a ser executado após a execução
    # da View que irá processar a requisição

        return response

    return middleware


# E como Classe:


class MiddlewareSimples:

    def __init__(self, get_response):
        self.get_response = get_response

        # Código de inicialização do Middleware

    def __call__(self, request):

        # Código a ser executado antes da View e
        # antes de outros middlewares serem executados

        response = self.get_response(request)

        # Código a ser executado após a execução
        # da View que irá processar a requisição

        return response
"""

# ---------------------------------------------------------------------------

"""
Vamos supor que queremos um middleware que filtre requisições
e só processe aquelas que venham de uma determinada lista de IP’s.
Esse middleware é muito útil quando temos, por exemplo, um
conjunto de servidores com IP fixo que vão se conectar entre si. Você
poderia, por exemplo, ter uma configuração no seu settings.py
chamada ALLOWED_SERVERS contendo a lista de IP autorizados a se
conectar ao seu serviço.
Para isso, precisamos abrir o cabeçalho das requisições que
chegam no nosso servidor e verificar se o IP de origem está autorizado.
Como precisamos dessa lógica antes da requisição chegar na View,
vamos adicioná-la ao método process_view , da seguinte forma:
"""

# FILTRA IP MIDDLEWARE
# ----------------------------------------


class FiltraIPMiddleware:

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Lista de IPs autorizados
        ips_autorizados = ['127.0.0.1']

        # IP do usuário
        ip_usuario = request.META.get('REMOTE_ADDR')

        # Verifica se é um IP autorizado
        if ip_usuario not in ips_autorizados:
            # Se não for
            return HttpResponseForbidden("IP não autorizado")

        # Se for um IP autorizado, não fazemos nada
        return None

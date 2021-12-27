from django import forms
from website.funcionarios.models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_servico',
            'remuneracao'
        ]

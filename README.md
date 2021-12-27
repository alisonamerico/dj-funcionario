# dj-funcionario
Aplicativo Django para gerenciamento de Funcionários (é possível adicionar, listar, atualizar e deletar).

## Instalação

Primeiro, recomenda-se a criação de um ambiente virtual.
```bash
python3 -m venv .venv
```

Com seu ambiente virtual configurado, instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate
```

## Execução

Para executar o servidor de testes do Django, execute:

```bash
python manage.py runserver
```

import json
from datetime import datetime

# aqui é a funções para manipulação de arquivos JSON
def guardar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4) 
#indent=4: define o nível de indentação para o JSON. 4 significa que cada nível de aninhamento nos dados JSON será recuado por 4 espaços
# aqui é a Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = {"senha": senha, "atividades": []}
    salvar_dados('usuarios.json', usuarios)
    print("Usuário cadastrado com sucesso!")

# na parte de "atividade" é a atividade que vai ser cadastrada     
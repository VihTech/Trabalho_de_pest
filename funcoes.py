import json

def adicionar_atualizar(dicionario, nome, matricula):
    if len(nome.split()) < 2 or nome.isalnum():
        return '\n--- O nome deve ser composto e não pode conter números ---'

    else:  

        if not matricula.isnumeric():
            return '\n--- A matricula deve conter apenas números  ---'
        else:
            dicionario[matricula] = nome
            return True
    
def visualizar(dicionario, tabela):
    print(f'========= {tabela:^16} =========')
    print('=-' * 18 + '=')
    print(f"{'|Nome:':<20} {'|Matricula:':>16}")
    for itens, valores in dicionario.items():    
        print('-'*37)
        print(f'|{valores:<24} |{itens:>5}')
    print('=-' * 18 + '=\n')

def tratamento_repetido(dicionario, matricula):
    if matricula not in dicionario:
        return True
    else:
        return False

def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)

def pegar_dicionario(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)
        
def valor_existente(valor, dicionario):
    if valor not in dicionario:
        return False
    else:
        return True
    
def excluir(dicionario, matricula, nome_do_arquivo):
    dicionario.pop(matricula)
    salvar_dicionarios(dicionario, nome_do_arquivo)

def criar_turma(dicionario, disciplina, professor, lista_alunos):
    dicionario_vazio = {}
    dicionario_vazio[professor] = lista_alunos
    dicionario[disciplina] = dicionario_vazio


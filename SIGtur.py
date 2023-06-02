from menus import*
from funcoes import*

#teste

# Dicionarios

dicionario_turma = dict()
dicionario_professor = dict()
dicionario_aluno = dict()

while True:
    escolha = menu_principal()
    if escolha == '1':
        escolha_do_coordenador = menu_do_coordenador()
        
        while True:
            
            if escolha_do_coordenador == '1':
                pass

            elif escolha_do_coordenador == '2':
                pass

            elif escolha_do_coordenador == '3':
                pass

            elif escolha_do_coordenador == '4':
                pass

            elif escolha_do_coordenador == '0':
                break

    elif escolha == '2':

        while True:
            escolha_do_professor = menu_de_professores()
        
            if escolha_do_professor == '1':
                while True:
                    nome = input('\n>>> Digite o nome do professor que deseja adicionar: ')
                    matricula = int(input(f'>>> Digite a matricula do professor {nome}: '))
                    retorno = adicionar_atualizar(dicionario_professor, nome, matricula)
                    if retorno == 'concluido':
                        print('\n --- Cadastro realizado com sucesso ---')
                        break
                    else:
                        print(retorno)

                
            elif escolha_do_professor == '2':
                while True:
                    nome = input('\n>>> Digite o nome do professor que deseja editar: ')
                    matricula = int(input(f'>>> Digite a matricula do professor {nome}: '))
                    if adicionar_atualizar(dicionario_professor, nome, matricula):
                        print('\n --- Cadastro realizado com sucesso ---')
                        break
                    else:
                        print('\n --- O nome deve ser composto e não pode conter números ---')

            elif escolha_do_professor == '3':
                pass

            elif escolha_do_professor == '4':
                pass

            elif escolha_do_professor == '5':
                pass

            elif escolha_do_professor == '6':
                visualizar(dicionario_professor)

            elif escolha_do_professor == '0':
                break

    elif escolha == '3':
        
        while True:
            escolha_do_aluno = menu_de_alunos()
    
            if escolha_do_aluno == '1':
                while True:
                    nome = input('\n>>> Digite o nome do aluno que deseja adicionar: ')
                    matricula = int(input(f'>>> Digite a matricula do aluno {nome}: '))
                    if adicionar_atualizar(dicionario_aluno, nome, matricula):
                        print('\n --- Cadastro realizado com sucesso ---')
                        break
                    else:
                        print('\n --- O nome deve ser composto e não pode conter números ---')
                
            elif escolha_do_aluno == '2':
                pass

            elif escolha_do_aluno == '3':
                visualizar(dicionario_aluno)

            elif escolha_do_aluno == '4':
                pass

            elif escolha_do_aluno == '5':
                pass

            elif escolha_do_aluno == '0':
                break

    elif escolha == '0':
        print('\n -- Programa encerrado! 😢🖐 --')
        break
    else:
        print('\n-- Oops! Parece que a opção selecionada não existe! Tente outra! --')

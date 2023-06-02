from menus import*
from funcoes import*

# Dicionarios

dicionario_turma = pegar_dicionario('turmas')
dicionario_professor = pegar_dicionario('professores')
dicionario_aluno = pegar_dicionario('alunos')

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
                    matricula = input(f'>>> Digite a matricula do professor {nome}: ')
                    retorno = adicionar_atualizar(dicionario_professor, nome, matricula)
                    if retorno == True:
                        print('\n --- Cadastro realizado com sucesso ---')
                        salvar_dicionarios(dicionario_professor, 'professores')
                        break
                    else:
                        print(retorno)
                
            elif escolha_do_professor == '2':
                while True:

                    visualizar(dicionario_professor)
                    matricula = input('\n>>> Digite a matricula do professor que deseja editar: ')
                    nome = input('>>> Digite novo nome do professor: ')

                    if valor_existente(matricula, dicionario_professor):

                        retorno = adicionar_atualizar(dicionario_professor, nome, matricula)
                        if retorno:
                            print('\n --- Atualização realizado com sucesso ---')
                            salvar_dicionarios(dicionario_professor, 'professores')
                            break
                        else:
                            print(retorno)
                    else:
                        print('\n--- Matricula Invalida ---\n')

            elif escolha_do_professor == '3':
                visualizar(dicionario_professor)

            elif escolha_do_professor == '4':

                while True:
                    visualizar(dicionario_professor)
                    matricula = input('\n>>> Digite a matricula do professor que deseja excluir: ')
                    if valor_existente(matricula, dicionario_professor):
                        excluir(dicionario_professor, matricula, 'professores')
                        print('\n--- Professor excluido com sucesso ---')
                        break
                    else:
                        print('\n--- Matricula Invalida ---\n')

            elif escolha_do_professor == '5':
                pass

            elif escolha_do_professor == '6':
                pass

            elif escolha_do_professor == '0':
                break

    elif escolha == '3':
        
        while True:
            escolha_do_aluno = menu_de_alunos()
    
            if escolha_do_aluno == '1':
                while True:
                    nome = input('\n>>> Digite o nome do aluno que deseja adicionar: ')
                    matricula = input(f'>>> Digite a matricula do aluno {nome}: ')
                    retorno = adicionar_atualizar(dicionario_aluno, nome, matricula)
                    if retorno == True:
                        print('\n --- Cadastro realizado com sucesso ---')
                        salvar_dicionarios(dicionario_aluno, 'alunos')
                        break
                    else:
                        print(retorno)
                
            elif escolha_do_aluno == '2':
                while True:

                    visualizar(dicionario_aluno)
                    matricula = input('\n>>> Digite a matricula do aluno que deseja editar: ')
                    nome = input('>>> Digite o novo nome do aluno: ')

                    if valor_existente(matricula, dicionario_aluno):

                        retorno = adicionar_atualizar(dicionario_aluno, nome, matricula)
                        if retorno:
                            print('\n --- Atualização realizado com sucesso ---')
                            salvar_dicionarios(dicionario_aluno, 'alunos')
                            break
                        else:
                            print(retorno)
                    else:
                        print('\n--- Matricula Invalida ---\n')

            elif escolha_do_aluno == '3':
                visualizar(dicionario_aluno)

            elif escolha_do_aluno == '4':
                 while True:
                    visualizar(dicionario_aluno)
                    matricula = input('\n>>> Digite a matricula do aluno que deseja excluir: ')
                    if valor_existente(matricula, dicionario_aluno):
                        excluir(dicionario_aluno, matricula, 'alunos')
                        print('\n--- Aluno excluido com sucesso ---')
                        break
                    else:
                        print('\n--- Matricula Invalida ---\n')

            elif escolha_do_aluno == '0':
                break

    elif escolha == '0':
        print('\n -- Programa encerrado! 😢🖐 --')
        break
    else:
        print('\n-- Oops! Parece que a opção selecionada não existe! Tente outra! --')

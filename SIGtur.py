from menus import*
from funcoes import*

# Dicionarios

dicionario_turma = pegar_dicionario('turmas')
dicionario_professor = pegar_dicionario('professores')
dicionario_aluno = pegar_dicionario('alunos')
#teste

while True:
    escolha = menu_principal()
    if escolha == '1':
    
        while True:
            escolha_do_coordenador = menu_do_coordenador()
            if escolha_do_coordenador == '1':
                condicional = True
                while condicional:
                    alunos = []
                    disciplina = input('\n>>> Digite a disciplina: ')

                    if disciplina not in dicionario_turma:
                        visualizar(dicionario_professor, 'Professores')
                        professor = input('\n>>> Matricula do professores da disciplina: ')

                        if professor.isnumeric():
                            
                            if professor in dicionario_professor:


                                visualizar(dicionario_aluno, 'Alunos')
                                while True:
                                    matricula_aluno = input('\n>>> Digite a matricula do alunos que deseja adicionar a turma: ')

                                    if matricula_aluno.isnumeric():
                                        if matricula_aluno in dicionario_aluno:
                                            if not dicionario_aluno[matricula_aluno] in alunos:
                                                alunos.append(dicionario_aluno[matricula_aluno])
                                                continuar = input('\n>>> Adicionar mais alunos? [s]im ou [n]ão: ')
                                                if continuar in 'Ss':
                                                    continue

                                                elif continuar in 'Nn':
                                                    criar_turma(dicionario_turma, disciplina, dicionario_professor[professor], alunos)
                                                    salvar_dicionarios(dicionario_turma, 'turmas')
                                                    print('\n--- Turma criada com sucesso ---')
                                                    condicional = False
                                                    break
                                                    
                                                else:
                                                    print('\n--- Valor Inválido ---')

                                            else:
                                                print('\n--- Alunos já está na turma ---')

                                        else:
                                            print('\n--- Matricula não existe ---')

                                    else:
                                        print('\n--- Matricula invalida ---')
                            else:

                                print('\n--- Matricula não existe ---')

                        else:
                            print('\n--- Matricula invalida ---')
                
                    else:
                        print('\n--- Esssa disciplina já possui uma turma')

            elif escolha_do_coordenador == '2':
                pass

            elif escolha_do_coordenador == '3':
                print('\n========= TURMAS =========\n')
                
                for chaves, valores in dicionario_turma.items():
                    print('=-' * 12 + '=')
                    print(f'>>> {chaves}')
                    for professor, lista in valores.items():
                        print(f'\t>>> Professor: {professor}')
                        for matricula, nome in dicionario_aluno.items():
                            for nomes in lista:
                                if dicionario_aluno[matricula] == nomes:
                                    print(f'\t\t{matricula} - {nomes}')


            elif escolha_do_coordenador == '4':
                posicao_do_valor = []
                index = 0
                for chaves, valores in dicionario_turma.items():
                    print(f'{index} - {chaves}')
                    posicao_do_valor.append(chaves)
                    index += 1

                while True: 
                    escolha = input('\n>>> Escolha a turma que deseja apagar: ')
                    if int(escolha) > len(posicao_do_valor) or not escolha.isnumeric():
                        print('\n--- Valor Inválido ---')
                    else:
                        dicionario_turma.pop(posicao_do_valor[int(escolha)])
                        print('\n--- Turma apagada com sucesso ---')
                        salvar_dicionarios(dicionario_turma, 'turmas')
                        break


            elif escolha_do_coordenador == '0':
                break

    elif escolha == '2':

        while True:
            escolha_do_professor = menu_de_professores()
        
            if escolha_do_professor == '1':
                while True:
                    nome = input('\n>>> Digite o nome do professor que deseja adicionar: ')
                    matricula = input(f'>>> Digite a matricula do professor {nome}: ')

                    if tratamento_repetido(dicionario_professor, matricula):
                        retorno = adicionar_atualizar(dicionario_professor, nome, matricula)
                        if retorno == True:
                            print('\n --- Cadastro realizado com sucesso ---')
                            salvar_dicionarios(dicionario_professor, 'professores')
                            break
                        else:
                            print(retorno)
                    else:
                        print('\n--- Essa matricula já está sendo ultilizada ---')
                
            elif escolha_do_professor == '2':
                while True:

                    visualizar(dicionario_professor, 'Professores')
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
                visualizar(dicionario_professor, 'Professores')

            elif escolha_do_professor == '4':

                while True:
                    visualizar(dicionario_professor, 'Professores')
                    matricula = input('\n>>> Digite a matricula do professor que deseja excluir: ')
                    if valor_existente(matricula, dicionario_professor):
                        excluir(dicionario_professor, matricula, 'professores')
                        print('\n--- Professor excluido com sucesso ---')
                        salvar_dicionarios(dicionario_professor, 'professores')
                        break
                    else:
                        print('\n--- Matricula Invalida ---\n')

            elif escolha_do_professor == '5':
                lista_de_turmas = []
                visualizar(dicionario_professor, 'Professores')
                escolha = input('\n>>> Escolha um professor para visualizar as turmas: ')
                for disciplina, valores in dicionario_turma.items():
                    if dicionario_professor[escolha] in valores:
                        lista_de_turmas.append(disciplina)
                if len(lista_de_turmas) > 0:
                    print('\n====== TURMAS ======')
                    for valores in lista_de_turmas:
                        print(f'> {valores}')
                else:
                    print('\n--- Esse professor não possui turmas ---')
                        


            elif escolha_do_professor == '6':
                dicionario_de_turmas = {}
                visualizar(dicionario_professor, 'Professores')
                escolha = input('\n>>> Escolha um professor para visualizar as turmas: ')
                for disciplina, valores in dicionario_turma.items():
                    if dicionario_professor[escolha] in valores:
                        dicionario_de_turmas[disciplina] = valores
                if len(dicionario_de_turmas) > 0:
                    print('\n====== ALUNOS ======')
                    for disciplina, valores in dicionario_de_turmas.items():
                        for chave, lista in valores.items():
                            print(f'>>> {disciplina}')
                            for alunos in lista:
                                print(f'\t- {alunos}')
                else:
                    print('\n--- Esse professor não possui turmas ---')
                        


            elif escolha_do_professor == '0':
                break

    elif escolha == '3':
        
        while True:
            escolha_do_aluno = menu_de_alunos()
    
            if escolha_do_aluno == '1':
                while True:
                    nome = input('\n>>> Digite o nome do aluno que deseja adicionar: ')
                    matricula = input(f'>>> Digite a matricula do aluno {nome}: ')

                    if tratamento_repetido(dicionario_aluno, matricula):

                        retorno = adicionar_atualizar(dicionario_aluno, nome, matricula)
                        if retorno == True:
                            print('\n --- Cadastro realizado com sucesso ---')
                            salvar_dicionarios(dicionario_aluno, 'alunos')
                            break
                        else:
                            print(retorno)
                    else:
                        print('\n--- Essa matricula já está sendo ultilizada ---')
                               
            elif escolha_do_aluno == '2':
                while True:

                    visualizar(dicionario_aluno, 'Alunos')
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
                visualizar(dicionario_aluno, 'Alunos')

            elif escolha_do_aluno == '4':
                 while True:
                    visualizar(dicionario_aluno, 'Alunos')
                    matricula = input('\n>>> Digite a matricula do aluno que deseja excluir: ')
                    if valor_existente(matricula, dicionario_aluno):
                        excluir(dicionario_aluno, matricula, 'alunos')
                        print('\n--- Aluno excluido com sucesso ---')
                        salvar_dicionarios(dicionario_aluno, 'alunos')
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

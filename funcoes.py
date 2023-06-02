def adicionar_atualizar(dicionario, nome, matricula):

    if len(nome.split()) < 2 or nome.isnumeric():
        return False

    else:  
        dicionario[nome] = matricula
        return True
    
def visualizar(dicionario):
    print('=-' * 15 + '=')
    print(f"{'Nome':^15} {'Matricula':>15}")
    for itens, valores in dicionario.items():    
        print(f'{itens:<15} {valores:^21}')
    print('=-' * 15 + '=\n')

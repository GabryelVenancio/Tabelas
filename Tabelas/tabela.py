funcionarios = []

funcionario = input('Funcionário? ')
while funcionario != '':
    funcionario = funcionario.split(';')
    funcionario[1] = float(funcionario[1])
    funcionario[2] = int(funcionario[2])
    if funcionario[3] == 'sim':
        funcionario[3] = True
    else:
        funcionario[3] = False    
    funcionarios.append(funcionario)
    funcionario = input('Funcionário? ')
print('-' * 45)
print(f'{"NOME":^16} | {"SALARIO":^11} | TEMPO | META')
print('-' * 45)
for funcionario in funcionarios:
    print(f'{funcionario[0]:16}', end=' | ')
    print(f'R$ {funcionario[1]:8.2f}', end=' | ')
    print(f'{funcionario[2]:^5}', end=' | ')
    if funcionario[3] == True:
        print(f'{"😍":^4}')
    else:
        print(f'{"😢":^4}')
print('-' * 45)      

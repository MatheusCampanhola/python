
'''
Exemplos de input/print

[1] Exemplo de print antigo (2.x)

print('Qual seu nome? ')
nome = input('R: ')

print('Seja bem vindo(a) %s' % nome)

print('Qual sua idade? ')
idade = input('R: ')

print('A %s tem %s anos.' % (nome, idade))

[2] Exemplo de print moderno (3.x)

print(f'Qual seu nome?')
nome = input('R: ')

print(f'Seja bem vindo(a) {nome}') ou
print(''Seja bem vindo(a) {}' .format(nome)) f = .format

print('Qual sua idade? ')
idade = input('R: ')

print(f'A {nome} tem {idade} anos.') ou
print(''A {} tem {} anos.' .format(nome, idade)) f = .format

[3] Exemplo de print "mais moderno"

print(f'A {nome} tem {2018 - int(idade)') -> cast

Cast -> conversão de um tipo de dado para outro.

[4] Forma mais correta de se usar

nome = int(input("Qual seu nome?\n")) -> \n pula linha
idade = int(input("Qual sua idade?\n")) -> \n pula linha

print(f'Bem vinda(a) {nome}, você tem {idade} anos.')
'''

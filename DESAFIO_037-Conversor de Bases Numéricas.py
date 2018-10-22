print('=====================DESAFIO_037=====================')
print('''Escreva um programa que leia um numero inteiro qualquer
e peça para o usuario escolher qual será o bloco de conversão
 1 para binario
 2 para octal
 3 para hexadecimal''')
print ('=====================PROGRAMA=======================')
num = int(input('Digite um número inteiro: '))
print ('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcão =int(input('Sua opcão: '))
if opcão == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num,bin(num)[2:]))
elif opcão == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcão ==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida tente novamente ')
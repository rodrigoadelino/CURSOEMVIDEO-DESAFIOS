print('=====================DESAFIO_069=======================')
print('''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer 
ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.''')
print('======================PROGRAMA=======================')
cmaior = csexo = cmulher = 0
while True:
    print('='*30)
    print('     CADASTRE UMA PESSOA     ')
    print('='*30)
    idade=int(input('Idade: '))
    if idade >= 18:
        cmaior += 1
    sexo=str(input('Sexo [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        csexo += 1
    if sexo == 'F' and idade <20:
        cmulher += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    print('='*30)
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('='*30)
print('Total de pessoas com mais de 18 anos:{}'.format(cmaior))
print('Ao todo temos um {} Homem(Homens) cadastrado(s)'.format(csexo))
print('E Temos {} Mulher(mulheres) com menos de 20 anos'.format(cmulher))
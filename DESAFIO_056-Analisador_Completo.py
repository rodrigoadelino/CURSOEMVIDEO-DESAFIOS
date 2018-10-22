print('=====================DESAFIO_56=====================')
print('''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 21 anos''')
print ('=====================PROGRAMA======================')
media=0
mvelho=0
mediaf=0
for pessoa in range (1,5):
    print('--------{}º PESSOA-----------'.format(pessoa))
    nome=(str(input('Nome: ')))
    idade=(int(input('Idade: ')))
    sexo=(str(input('Sexo [M/F]: '))).upper()
if  idade > media:
    media = media +(idade)/2
if  idade > mvelho  and sexo == 'M':
    enome=(nome)
    mvelho =+ idade
if  idade >1 <21 and sexo == 'F':
    mediaf =+ pessoa     
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(mvelho,enome))
print('Ao todo são {} mulheres com menos de 21 anos'.format(mediaf))
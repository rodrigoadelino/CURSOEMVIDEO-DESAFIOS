print('==================DESAFIO_076===================')
print('''Crie um programa que tenha uma tupla única com 
nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando 
os dados em forma tabular.''')
print('==================PROGRAMA===================')
listagem = ('Lapis',1.75,
            'borracha',2,
            'caderno',15)

print('-'*20)
print('{:^20}'.format('LISTAGEM DE PRECOS'))
print('-'*20)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:           
        print(f'{listagem[pos]:.<17}',end='')
    else:
        print(f'R${listagem[pos]:>7}')

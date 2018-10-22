print('=====================DESAFIO_070=======================')
print('''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. ''')
print('======================PROGRAMA=======================')
print('=' * 30)
print('     LOJA SUPER BARATÃO     ')
print('=' * 30)
total= cont= mmil =0
barato=''
while True:
    produto=str(input('Nome do Produto: '))
    preco=int(input('Preço: R$: '))
    cont += 1
    total += preco
    if preco > 1000:
        mmil += 1
    if cont == 1 or preco < menor:  #Dessa forma
       menor = preco                #Fica
       barato = produto             #Menor
    #if cont == 1
    #    menor = preco
    #else:
    #    if preco < menor:
    #        menor = preco
    #        barato = produto
    resp=str(input('Quer continuar? ' )).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break

print('O total da compra foi de R$:{:.2f}'.format(total))
print('Temos {} produto(s) custando mais de R$ 1000.00'.format(mmil))
print('O Produto mais barato foi {} que custa R$:{} '.format(barato,menor))

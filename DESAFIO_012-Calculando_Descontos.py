print ('='*25,'DESAFIO_12','='*26)
print ('='*5,'Faça um algoritmo que leia o preço de um produto ','='*7)
print ('='*10,'E mostre seu novo preço,com 5% de desconto','='*10)
p=float(input('\nDigite o valor do Produto: '))
n=p*5/100
d=p-n
print('O valor do produto é {}\nCom o desconto de 5%\nO Produto passa valer {:.2f}'.format(p,d))

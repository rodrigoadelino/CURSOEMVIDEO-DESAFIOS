print ('='*25,'DESAFIO_13','='*25)
print ('='*5,'Faça um algoritmo que leia o salario de um funcionario ','='*5)
print ('='*10,'E mostre seu novo salario, com 15% de aumento','='*10)

s=float(input('\nDigite seu salario: '))
p=s*15/100
n=p+s
print ('Seu salario é de R${}\nCom o aumento de 15%\nVoce passara a receber R$ {:.2f}'.format(s,n))


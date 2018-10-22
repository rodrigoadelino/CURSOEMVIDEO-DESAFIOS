print('================DESAFIO_034===================')
print('''faça um programa que pergunte o salario de um funcionario 
e calcule o valor do seu aumentoPara salarios superiores a R$ 1.250,00
calcule um aumento de 10% Para os inferiores ou iguais o aumento 
é de 15%''')
print('================PROGRAMA=>==================')
s=float(input('Qual é valor do seu salario?: '))
p1=s*10/100
p2=s*15/100
if s >1250.00:
   print('O Salario com o aumento será de R$ {}'.format(p1+s))
if s <=1250.00:
   print('O Salario com o aumento será de R$ {}'.format(p2+s))



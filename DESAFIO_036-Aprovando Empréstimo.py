print('=====================DESAFIO_036=====================')
print('''Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então 
o empréstimo será negado.''')
print ('=====================PROGRAMA=======================')
casa=float(input('Qual o valor da casa? '))
salario=float(input('Qual o seu salario? '))
anos=int(input('Em quantos anos pretende pagar? '))
parcela=((casa/anos)/12)
print('\nPara pagar uma casa de R$ {:.2f} em {} anos\nA prestação será de R${:.2f}'.format(casa,anos,parcela))
if parcela >(salario*30/100):
    print('EMPRESTIMO NEGADO')
if parcela==(salario*30/100):
    print('EMPRESTIMO CONCEDIDO NO LIMITE')
elif parcela <(salario*30/100):
    print('EMPRESTIMO CONCEDIDO')




print('==================DESAFIO_071===================')
print('''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.''')
print('==================PROGRAMA===================')
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor=int(input('Informe o valor quer sacar: '))
total=valor
ced=50
ccedu=0
while True:
    if total >= ced:
       total -= ced
       ccedu +=1
    else:
       if ccedu > 0:
          print (ccedu,ced )
       if ced ==50:
          ced =20
       elif ced ==20:
            ced=10
       elif ced == 10:
            ced =1
       ccedu =0
       if total == 0:
          break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
       

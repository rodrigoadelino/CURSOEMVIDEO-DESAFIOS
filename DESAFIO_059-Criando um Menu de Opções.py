print('========DESAFIO 059========')
print('''Crie um programa que leia dois 
valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa devera realizar a 
operacao solicitada em cada caso''')
print('=======PROGRAMA==========')
n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
op=''
while op!=5:
      print('''    ====menu====
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
    ============''')
      op=int(input('\nDigite a opção desejada: '))
      if op==4:
         n1=int(input('\nDigite o primeiro número: '))
         n2=int(input('Digite o segundo número: '))
      if op==1:
         print('Resposta: {} + {}  = {}'.format (n1,n2,(n1+n2)))
      if op==2:
         print('Resposta: {} X {}  = {}'.format (n1,n2,(n1*n2)))
      if op==3:
         if n1>n2:
            print('O primeiro numero {} é o maior'.format(n1))
         if n2>n1:
            print('O segundo numero {} é  o maior'.format(n2))
         if n1==n2:
            print('Os numeros sao iguais')
      if op >5:
         print('Opção invalida')
        

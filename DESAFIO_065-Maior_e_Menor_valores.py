print('========DESAFIO_065======')
print('''Crie um programa que leia vários 
números inteiros pelo teclado,
no final da execução, mostre a 
média entre todos o valores e qual
foi o maior e o menor valores lidos. 
O programa deve perguntar
ao usuário se ele quer ou não 
continuar a digitar valores''')
print('========PROGRAMA========')
p='s'
total= cont = maior = menor = 0
while p not in 'Nn':
      n=int(input('Digite um número: '))
      total+=n
      cont+=1
      if cont == 1:
         menor = maior = n
      else:
         if n < menor:
            menor = n
         if n > maior:
            maior = n
      p=str(input('deseja continuar[s/n]: '))
media=total/cont     
print('Voce digitou {} numeros e a media foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format (maior, menor))
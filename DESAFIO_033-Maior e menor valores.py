n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
n3=int(input('Digite o terceiro número : '))
#if n1>n2 and n1>n3:
#   print('O primeiro numero é o maior')
#if n2>n1 and n2>n3:
#   print('O segundo número é o maior')
#if n3>n1 and n3>n2:
#   print('O terceiro número é o maior')
menor=n1
if n2<n1 and n2<n3:
   menor=n2
if n3<n1 and n3<n2:
   menor=n3
print('\nO menor valor digitado foi {}'.format(menor))
maior=n1
if n2>n1 and n2>n3:
   maior=n2
if n3>n1 and n3>n2:
   maior=n3
print('O maior valor digitado foi {}'.format (maior))
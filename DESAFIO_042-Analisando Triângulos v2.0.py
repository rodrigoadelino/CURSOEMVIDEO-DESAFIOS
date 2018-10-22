print('=====================DESAFIO_042=====================')
print('''Refaça o DESAFIO 035 dos triângulos, acrescentando 
o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes''')
print ('=====================PROGRAMA=======================')
a=float(input('Digite o comprimento da primeira reta: '))
b=float(input('Digite o comprimento da segunda  reta: '))
c=float(input('Digite o comprimento da terceira reta: '))
if a<b+c and b<a+c and c<a+b:
   print('Os segmentos acima podem formar um triângulo ', end ='')
   if a == b == c :
      print('EQUILÁTERO!')
   elif a != b != c != a:
      print('ESCALENO!')
   else:
      print('ISÓSCELES')
else:
    print('Os segmentos acima nao podem formar um triângulo')


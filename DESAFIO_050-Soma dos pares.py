soma=0
cont=1
for c in range (0,7):
    n=int(input('Numero'))
    if n % 2 == 0:
       soma= soma + n
       cont= cont + n
print('Vc digitou {}\nnúmeros e a soma dos números pares é {}'.format(cont,soma))
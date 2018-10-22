cont=1
soma=0
for n in range(1,500,2):
    if n % 3 == 0:
       soma= soma + n
print ('A soma dos numeros impares\nE multiplos de 3 é {}'.format(soma))
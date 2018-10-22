n=int(input('Digite o número: '))
tot=0
for c in range (1,n +1):
    if n % c == 0:
       print('\033[34m', end=' ')
       tot += 1
    else:
       print('\033[32m', end=' ')
    print('{}'.format (c), end=' ')
print ('\n\033[mO numero {} foi dividido {} vezes'.format (c,tot,end=' '))
if tot == 2:
   print('É um número PRIMO')
else:
   print('Não é um número PRIMO')
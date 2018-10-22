frase=str(input('digite uma frase: ')).strip() .upper()
separado=(frase.split())
junto=(''.join(separado))
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('frase normal é {}\nfrase invertida {}'.format (junto,inverso))
if junto == inverso:
   print('temos um PALINDROMO')
else:
   print('nao temos um PALINDROMO')

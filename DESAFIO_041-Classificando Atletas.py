print('=====================DESAFIO_041=====================')
print('''A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER''')
print ('=====================PROGRAMA=======================')
ano=int(input('Digite o ano de nascimento: '))
id=2018-ano
if id<=9:
   print('voce tem {} anos\nsua categoria é mirim'.format(id))
elif id>=10 and id<=14:
   print('voce tem {} anos\nsua categoria é infatil'.format(id))
elif id>=15 and id<=19:
   print('voce tem {} anos\nsua categoria é Junior'.format (id))
elif id==20:
   print('voce tem {} anos\nsua categoria é Senior'.format (id))
else:
   print('Voce tem {} anos\nsua categoria é Master'.format (id))
   

#print(id)
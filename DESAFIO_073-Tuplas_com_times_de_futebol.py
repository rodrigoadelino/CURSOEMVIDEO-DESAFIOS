print('==================DESAFIO_073===================')
print('''Exercício Python 073: Crie uma tupla preenchida 
com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.''')
print('==================PROGRAMA===================')
lista=('Palmeiras','Corithians','Chapecoense','Santos','Vasco','Sao Paulo')
print('Lista de times do Brasileirão: {}'.format (lista))
print ('='*30)
print('Os 5 primeiros são:{}'.format(lista[0:5]))
print('='*30)
print('Os 4 ultimos são :{}'.format(lista[-4:]))
print ('='*30)
print('Times em ordem alfabética {}'.format(sorted(lista)))
print('='*30)
print('A Chapecoense esta na {}º posição'.format(lista.index("Chapecoense")+1))

#for pos in lista ([3]):
 #   print (pos)
#for c in enumerate(lista):
    
  #  print (c)
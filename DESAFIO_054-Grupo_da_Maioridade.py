totalmaior=0
totalmenor=0
for pessoa in range (1,4):
    n=int (input('Ano de nascimento da {}¤ pessoa: '.format (pessoa)))
    idade=(2018 -n)
    #print('Quem nasceu em {} tem {} ano(s)'.format(n,idade))
    if idade > 21:
       totalmaior +=1
    else:
       totalmenor +=1
print ('temos {} pessoas que ja completou a maioridade'.format (totalmaior))
print ('temos {} pessoas que ainda nao completaram a maioridade'.format(totalmenor))
       
    
  



print ('=======DESAFIO 057==========')
print ('''faca um programa que leia
o sexo de uma pessoa mas so aceite
os valores M ou F caso esteja errado
peca a digitação novamente ate um 
valor correto\n''')

sexo=''
sexo=str(input('Informe o seu Sexo[M/F]: ')).upper().strip()#[0]
while sexo not in 'MF':
#while sexo !='M' and sexo!='F':
      sexo=str(input('Dados invalidos,Informe apenas [M ou F]: ')).upper().strip()#[0]
print('\nFIM o Sexo digitado foi {}'.format (sexo))
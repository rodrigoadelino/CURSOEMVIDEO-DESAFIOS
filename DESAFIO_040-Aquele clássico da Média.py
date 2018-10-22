print('=====================DESAFIO_040=====================')
print('''Crie um programa que leia duas notas de um aluno 
e calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO''')
print ('=====================PROGRAMA=======================')

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
if 7 > media >=5:
   print('sua media foi {}\nEsta entre 5.0 e 6.9 RECUPERAÇÃO'.format (media))
elif media <5.0:
   print('sua media foi {}\nabaixo de 5.0 REPROVADO'.format (media))
else:
   print('A média foi {}\nO aluno está APROVADO'.format (media))
   

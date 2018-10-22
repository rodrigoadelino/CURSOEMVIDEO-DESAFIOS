#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# USS 1,00 = R$3,27
print ('======DESAFIO 10======')
v=float(input('digite o valor em R$ que possui' ))
d= v//3.27
print ('Com R$ {} voce consegue comprar U${}'.format(v,d))

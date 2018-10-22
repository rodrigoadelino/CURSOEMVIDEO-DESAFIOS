print('=====================DESAFIO_044=====================')
print('''Elabore um programa que calcule o valor de um produto
considerando seu preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- À Vista no cartão: 5% de desconto
- Em até 2X no cartão preço normal
- Em 3X ou mais no cartão: 20% de juros''')
print ('=====================PROGRAMA======================')
p=float(input('\nQual o valor do produto R$? '))
print('\nFormas de Pagamentos\nOpção 1: À Vista (dinheiro/cheque) 10% de desconto\nOpção 2: À Vista no cartão 5% de desconto')
print('Opção 3: Em até 2X no cartão preço normal\nOpção 4: Em 3X ou mais no cartão 20% de desconto')
o=int(input('\nEscolha a opção de pagamento: '))
if o==1:
   print('\nVoce escolheu pagar à vista no dinheiro ou cheque\nO valor com desconto é de R$ {:.2f}'.format(p-(p*10/100)))
elif o==2:
   print('\nVoce escolheu pagar à vista no cartão\nO valor com desconto é de R${:.2f}'.format(p-(p*5/100)))
elif o==3:
   print('\nVoce escolheu em até 2X no cartao\nO valor da parcela será de  R${:.2f}\nForma de pagamento sem desconto'.format(p/2))
elif o==4:
    pa=int(input('Em Quantas vezes deseja parcelar?'))
    if o >= 3:
        print('\nVoce escolheu pagar em {}X\nO valor da parcela será de R${:.2f}\nO valor total do produto será de R${}'.format(pa,(p/pa),(p+(p*20/100))))
else:
    print('Opçao de pagamento invalida')
print('==================DESAFIO_077===================')
print('''Crie um programa que tenha uma tupla com várias 
palavras (não usar acentos). Depois disso, você deve mostrar,
 para cada palavra, quais são as suas vogais.
''')
print('==================PROGRAMA===================')
palavras=('aprender','python','PROGRAMAR','CURSO','Guanabara')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
           print (letras, end='')
t=int(input('digite o primeiro termo: '))
r=int(input('Digite a razao: '))
d=t + (10-1)*r
for c in range (t,d + r,r):
    
    print (c, end=' ')
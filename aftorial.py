print('digite um numero para')
a=int(input('calcular seu fatorial : '))
print('calculando {} '.format(a))
fat= 1
while (a>1):
    fat*=a
    a -= 1
print('o valor final da fatoração é : {}'.format (fat))

# from math import factorial
#a=int(input('digite um numero para saber seu fatorial : '))
#fac=factorial(a)
#print('o fatorial de {} é {}'.format(a,fac))
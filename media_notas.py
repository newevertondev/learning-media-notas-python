n1= float(input('Qual a primeira nota?'))
n2= float(input('Qual a segunda nota?'))
soma= (n1+n2)/2

print('A sua nota foi {}!!'.format(soma))

if soma >= 6:
    print('Aprovado!!')
else:
    print('Estude mais!!')

contador = 0

for num in range(10):
    numero = int(input('Informe um número: '))
par = numero % 2 == 0
for num in range(par):
    print('O número é par')
impar = numero % 2 != 0
for num in range(impar):
    print('O número é impar')
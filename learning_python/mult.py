#multiplicar dos numeros sin usar el asterisco

a = int(input('Escriba el primer numero \n'))
b = int(input('Escriba el segundo numero \n'))

total = 0
for i in range(a):
    total = total + b
print('El resultado es: ', total)

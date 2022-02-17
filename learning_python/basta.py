i = 0
total = 0
while i == 0:
    num = input('Ingrese el numero a sumar o "basta": ')
    if num != 'basta':
        total = int(num) + total
    else:
        break

print('el total de la suma es de: ', total)
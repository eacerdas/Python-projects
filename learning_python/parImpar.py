def parImpar(num):
    paridad = num % 2
    if paridad == 0: 
        return True
    else: 
        return False

numero = parImpar(242)
print('el numero es par') if numero == True else print('el numero es impar')


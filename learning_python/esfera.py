#devuelve el volumen de una esfera por su radio

def esfera(radio):
    area = (4/3) * 3.14 * radio ** 3
    return area
area = esfera(int(input('Escriba el radio')))
print('El area es: ', area)

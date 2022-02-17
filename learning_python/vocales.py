#cuantas vocales tiene una palabra

def vocales(palabra):
    cons = 0
    count = 0
    for x in palabra:
        i = x.lower()
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count = count + 1
        else:
            cons = cons + 1
    return count
numVocales = vocales(input('Escriba la palabra para contar sus vocales: ---> '))
print(numVocales)
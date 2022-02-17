#imprimir el elemento menor de una lista

lista1 = [7, -24, -13, 3, 4, 5, 2, 1, 8, 6, 9]

#primera solucion
def encontrarMenor1(lista):
    lista.sort()
    menor = lista[0]
    return menor

#otra forma
def encontrarMenor2(lista):
    menor2 = lista[0]
    for x in range(len(lista)):
        if menor2 > lista[x]:
            menor2 = lista[x]
    return menor2

#otra forma
def encontrarMenor3(lista):
    num = lista[0]
    for x in lista:
        if x < num:
            num = x
        else:
            num = num
    return num


menorlista = encontrarMenor3(lista1)
print (menorlista)


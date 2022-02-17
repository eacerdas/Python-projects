def mostrarListaRec(lista, indice):
    if indice < len(lista):
        print(lista[indice])
        indice = indice + 1
        mostrarListaRec(lista, indice)


lista = ['hola', 'chanchito', 'feliz']

mostrarListaRec(lista,0)
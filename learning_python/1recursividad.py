def sumaRec(num):
    if num == 1:
        return 1
    else:
        return num + sumaRec(num-1)
    
#si num == 5 => 5+4+3+2+1 = 15

suma = sumaRec(int(input('Escriba el numero a sumar: ')))
print('El total es', suma)




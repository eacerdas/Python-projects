#indica si eres mayor de edad

def mayor(edad):
    if edad < 18:
        return 'usted es menor de edad'
    else:
        return 'usted es mayor de edad'

mayorEdad = mayor(int(input('Escriba su edad:')))
print(mayorEdad)


#otra forma
def esMayor(usuario):
    if usuario.edad < 18:
        return False
    else:
        return True

class Usuario:
    def __init__(self, edad):
        self.edad = edad

#instancias de los usuarios, quiero 3

usuario1 = Usuario(-15)
mayor1 = esMayor(usuario1)
if mayor1 == True:
    print('El usuario1 es mayor')
else: 
    print('El usuario1 es menor')

usuario2 = Usuario(21)
mayor2 = esMayor(usuario2)
if mayor2 == True:
    print('El usuario2 es mayor')
else: 
    print('El usuario2 es menor')





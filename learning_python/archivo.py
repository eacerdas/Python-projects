#agrega el nombre y el apellido a un archivo con funcion por aparte


def guardaNombre(usuario):
    nombre = usuario.nombre
    apellido = usuario.apellido
    completo = nombre + ' ' + apellido

    archivo = open('archivo.txt', 'a')
    archivo.write(completo + '\n')
    archivo.close()


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def imprimir(self):
        print('El usuario ingresado es: ', self.nombre, self.apellido)

usuario1 = Usuario(str(input('Ingrese el nombre: ')),str(input('Ingrese el apellido: ')))

usuario1.imprimir()
guardaNombre(usuario1)


#otra forma usando la funcion como metodo de la clase
class Usuario:
    #atributos
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #metodos

    def imprimir(self):
        print('El usuario ingresado es: ', self.nombre, self.apellido)

    def guardaNombre(usuario):
        nombre = usuario.nombre
        apellido = usuario.apellido
        completo = nombre + ' ' + apellido

        archivo = open('archivo.txt', 'a')
        archivo.write(completo + '\n')
        archivo.close()

usuario1 = Usuario(str(input('Ingrese el nombre: ')),str(input('Ingrese el apellido: ')))

usuario1.imprimir()
usuario1.guardaNombre()
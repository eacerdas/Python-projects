//Herencia de clase Persona
//Edward Cerdas Rodríguez - B71956

class Persona: //Se define la clase Persona
    def __init___(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

//Se define la clase Estudiante que hereda de la clase Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, num_carne, nota):
        Persona.__init__(self, nombre, edad)
        self.num_carne=num_carne
        self.nota=nota


//Se define la clase EstudianteUniversitario que hereda de la clase Estudiante
class EstudianteUniversitario(Estudiante):
    def __init__(self, nombre, edad, num_carne, nota, carrera):
        Estudiante.__init__(self, nombre, edad, num_carne, nota)
        self.carrera=carrera

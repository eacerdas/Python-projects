//Herencia de clase Vehiculo
//Edward Cerdas Rodríguez - B71956

class Vehiculo: //Se define la clase Vehiculo
    def __init___(self, marca, color, año_fabricacion):
        self.marca=marca
        self.color=color
        self.año_fabricacion=año_fabricacion

//Se define la clase Moto que hereda de la clase Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, color, año_fabricacion, tipo_ruedas, cilindraje, tipo_motor):
        Vehiculo.__init__(self, marca, color, año_fabricacion)
        self.tipo_ruedas=tipo_ruedas
        self.cilindraje=cilindraje
        self.tipo_motor=tipo_motor

//Se define la clase Carro que hereda de la clase Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, color, año_fabricacion, num_puertas, tipo_combustible, num_cambios):
        Vehiculo.__init__(self, marca, color, año_fabricacion)
        self.num_puertas=num_puertas
        self.tipo_combustible=tipo_combustible
        self.num_cambios=num_cambios

//Se define la clase Bus que hereda de la clase Vehiculo
class Bus(Vehiculo):
    def __init__(self, marca, color, año_fabricacion, num_pasajeros, num_pisos, wifi):
        Vehiculo.__init__(self, marca, color, año_fabricacion)
        self.num_pasajeros=num_pasajeros
        self.num_pisos=num_pisos
        self.wifi=wifi

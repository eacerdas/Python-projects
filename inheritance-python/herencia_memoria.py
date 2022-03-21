//Herencia de clase Memoria
//Edward Cerdas Rodríguez - B71956

class Memoria: //Se define la clase Memoria
    def __init___(self, capacidad, precio):
        self.capacidad=capacidad
        self.precio=precio

//Se define la clase RAM que hereda de la clase Memoria
class RAM(Memoria):
    def __init__(self, capacidad, precio, tipo_ddr, frecuencia):
        Memoria.__init__(self, capacidad, precio)
        self.tipo_ddr=tipo_ddr
        self.frecuencia=frecuencia

//Se define la clase Cache que hereda de la clase Memoria
class Cache(Memoria):
    def __init__(self, capacidad, precio, tipo_cache):
        Memoria.__init__(self, capacidad, precio)
        self.tipo_cache=tipo_cache
    
//Se define la clase MemoriaPrincipal que hereda de la clase Memoria
class MemoriaPrincipal(Memoria):
    def __init__(self, capacidad, precio, tipo_conexion):
        Memoria.__init__(self, capacidad, precio)
        self.tipo_conexion=tipo_conexion


//Se define la clase HDD que hereda de la clase MemoriaPrincipal
class HDD(MemoriaPrincipal):
    def __init__(self, capacidad, precio, tipo_conexion, rpm):
        MemoriaPrincipal.__init__(self, capacidad, precio, tipo_conexion)
        self.rpm=rpm

//Se define la clase SDD que hereda de la clase MemoriaPrincipal
class SDD(MemoriaPrincipal):
    def __init__(self, capacidad, precio, tipo_conexion, velocidad_escritura, velocidad_lectura):
        MemoriaPrincipal.__init__(self, capacidad, precio, tipo_conexion)
        self.velocidad_escritura=velocidad_escritura
        self.velocidad_lectura=velocidad_lectura

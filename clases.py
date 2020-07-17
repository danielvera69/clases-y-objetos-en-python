class Persona:
    '''atributo de clase'''
    _siguiente = 0
    '''metodo de clase'''
    @staticmethod
    def parametros():
        return {"empresa":"UNEMI","direccion":"Km 1/2","Region":5}

    def __init__(self,nombre="Invitado",cedula="9999999999",activo=True):
        self.__codigo = self.siguiente()
        self.__nombre = self.__nombreMayuscula(nombre)
        self.__cedula = cedula
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self,ced):
        self.__cedula = ced

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod

    def mostrar_datos(self):
        return "Codigo: {} - Nombre: {} - Cedula: {} - Activo: {}".format(self.codigo, self.nombre, self.cedula,self.activo)

    def __nombreMayuscula(self, nombre=""):
        return nombre.upper()

    def siguiente(self):
        Persona._siguiente = Persona._siguiente + 1
        return Persona._siguiente

class Empleado(Persona):

    def __init__(self,nom,ced,act,sueldo=386):
        Persona.__init__(self,nom,ced,act)
        self.sueldo=sueldo

    def mostrar_datos(self):
        return Persona.mostrar_datos(self)+" - Sueldo: "+str(self.sueldo)



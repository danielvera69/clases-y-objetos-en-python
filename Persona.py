class Persona:
    _siguiente = 0
    def __init__(self, nom, ced="9999999999", act=True):
        self.nombre = nom
        self.cedula = ced
        self.activo = act

    def mostrar(self):
        return " Nombre: {} - Cedula: {} - Activo: {}".\
            format(self.nombre, self.cedula,self.activo)

# llamadas
# per1 = Persona("Daniel")
# per2 = Persona("Erick",'0912314569',False)
# print(per1.mostrar())
# personas = []
#
# for c in range(2):
#     nom = input("Ingrese Nombre")
#     ced = input("Ingrese Cedula")
#     per = Persona(nom,ced)
#     personas.append(per)
#
# for person in personas:
#     print(person.mostrar())

# Herencia
class Empleado(Persona):
    def __init__(self,nom,ced,act,sueldo=400):
        # Persona.__init__(self,nom,ced,act)
        super().__init__(nom,ced,act)
        self.sueldo=sueldo

    # @property
    # def sueldo(self):
    #     return self.__sueldo
    # @sueldo.setter
    # def sueldo(self, sue):
    #     self.__sueldo = sue

    def __jornada(self,dias=None):
        return self.sueldo if dias == None else self.sueldo/30*dias

    def mostrar(self):
        datos = super().mostrar()
        jornada1 = self.__jornada()
        jornada2 = self.__jornada(15)
        return " {} Jornada completa: ${:.2f} Jornada2: ${:.2f}".format(datos,jornada1,jornada2)

emp = Empleado("Daniel","0924192213",True)
emp.sueldo=600
print(emp.mostrar()+" Sueldo:"+str(emp.sueldo))

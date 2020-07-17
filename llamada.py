from clases import Persona,Empleado
'''per1 = Persona("Daniel")
per2 = Persona("Juan","0914192182")
per3 = Persona("Jose")
per4 = Persona(cedula="0912141899")
print(per1.mostrar_datos())
print(per2.mostrar_datos())
print(per3.mostrar_datos())
print(per4.mostrar_datos())
per1 = Persona("Daniel")
per2 = Persona("Juan","0914192182")
per3 = Persona("Jose")
per4 = Persona(cedula="0912141899")
print(per1.mostrar_datos())
print(per2.mostrar_datos())
print(per3.mostrar_datos())
print(per4.mostrar_datos())
personas = []
for c in range(2):
    nom = input("Ingrese Nombre")
    sue = input("Ingrese Cedula")
    per = Persona(nom,sue)
    personas.append(per)
#+str(float(person.sueldo)*float(Persona.parametros()["iess"])/100.00)
for person in personas:
    print(Persona.parametros()["empresa"])
    print(person.mostrar_datos())

'''
emp1 = Empleado("Daniel","099934334",True,500)
emp2 = Empleado("Juan","0914192182",True)

print(emp1.mostrar_datos())
print(emp2.mostrar_datos())

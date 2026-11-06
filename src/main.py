from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO
from dominio.departamento import Departamento
from persistencia.crear_bd import crear_tablas
crear_tablas()

emp = Empleado("correo@gmail.cl", "juanito")
print(emp.mostrar_datos())
EmpleadoDAO.insertar(emp)
print(emp.mostrar_datos())













# 
# emp2 = Empleado(
#         correo="julio@gmail.cl",
#         nombre="julio",
# )
# emp3 = Empleado("correo@gmail.cl", "juanito")

# print(emp.mostrar_datos())
# print(emp2.mostrar_datos())
# print(emp3.mostrar_datos())



# desarrollo = Departamento("Desarrollo")
# # Uso desde main.py
# desarrollo.agregar_empleado(emp)
# desarrollo.agregar_empleado(emp2)
# print("cantidad: ", desarrollo.cantidad_empleados())
# print("lista empleados")
# for empleado in desarrollo.empleados:
#         print(empleado.mostrar_datos())
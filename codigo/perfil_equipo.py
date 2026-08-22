nombreEquipo = input("Ingrese el nombre del equipo: ").upper()
comision = input("Ingrese la comisión del equipo: ")

nombres = []
roles = []

nombre = input("Ingrese el nombre del integrante (o 'fin' para terminar): ").title()
while nombre.lower() != "fin":
    rol = input(f"Ingrese su rol en el proyecto: ")
    nombres.append(nombre)
    roles.append(rol)
    nombre = input("Ingrese el nombre del integrante (o 'fin' para terminar): ").title()
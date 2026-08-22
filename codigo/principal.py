# codigo/principal.py
print("Primer programa del Proyecto Integrador")
texto = "Programacion en Python"

#a
print(texto[0])
print(texto[-1])

#b
print(texto[0:12])

#c
print(texto[::-1])

#d
if "Python" in texto:
    print("La palabra 'Python' se encuentra en el texto.")
else:
    print("La palabra 'Python' no se encuentra en el texto.")

#6
print("a:", texto.upper())
print("b:", texto.lower())
print("c:", texto.title())
print("d:", texto.capitalize())
print("e:", texto.replace("Python", "IA"))
print("f:", texto.count("a"))
print("g:", texto.find("Python"))
print("h:", len(texto))

#7
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad

#a
print(f"Producto: {producto}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Total: {total}")

#b
print("Producto: " + producto)
print("Precio unitario: " + str(precio))
print("Cantidad: " + str(cantidad))
print("Total: " + str(total))
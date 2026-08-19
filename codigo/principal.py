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

print("1:", texto.upper())
print("2:", texto.lower())
print("3:", texto.title())
print("4:", texto.capitalize())
print("5:", texto.replace("Python", "IA"))
print("6:", texto.count("a"))
print("7:", texto.find("Python"))
print("8:", len(texto))
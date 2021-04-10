#3. Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuántas veces aparece la letra A (mayúscula y minúscula)

miString = input("Introducir String: ")

longitud = len(miString)

A = miString.count("A")

a = miString.count("a")

print ("El tamaño del String es: ", longitud)

print ("La cantidad de a es: ", a)

print ("La cantidad de A es: ", A)

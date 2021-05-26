#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

#Cristian Pérez
numero_telefono = input("ingrese un numero telefonico: ")
substring_numero = numero_telefono[4:-3]
print(substring_numero)


#Juan Diego
numero_telefonico = (input("Introduzca un numero telefonico que empieze por +xx-xxxxxxxxx-xx: ")) 

numero2 = numero_telefonico[4:-3]
print(numero2)

#Juan David
numero = input("introduzca un numero telefonico con su respectivo prefijo y extension")
print(numero[4:-3])



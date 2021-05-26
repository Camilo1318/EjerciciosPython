
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

#Cristian Pérez
frase = input("Intoduzca una frase: ")
vocal = input("Introduzca una vocal que este incluida en la frase: ")

nueva_frase = frase.replace(vocal,vocal.upper())

print("La nueva frase es: ",nueva_frase)



#
txt = input("Ingrese una frase: ")
vocal_ingresada = input("Ingrese la vocal que quiere pasar a mayúscula dentro de la frase ingresada anteriormente: ")

resultado = txt.replace(vocal_ingresada,vocal_ingresada.upper())

print("El resultado obtenido es este: ", resultado)


#Juan Diego

texto = input("Introduzca una frase cualquiera: ")

vocal = input("Introduzca una vocal: ")

vocalup = vocal.upper()

reemplazo = texto.replace(vocal, vocalup)

print(f"La frase con la vocal es mayuscula es:{reemplazo}")



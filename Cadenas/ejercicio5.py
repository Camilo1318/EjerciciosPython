#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.



#Cristian Pérez
frase = input("Ingrese una frase, la que usted quiera: ")
length_frase = len(frase)
frase1 = frase[length_frase::-1]

print(f"La frase al reves, 1er Metodo: {frase1} ")
print(f"La frase al reves, 2do Metodo: {''.join(reversed(frase))}")

#Juan Diego

texto = input("Introduzca una frase cualquiera: ")
texto_corte = (texto[::-1])
texto_corte2 = ''.join(reversed(texto))

print(f""""
La frase es: {texto}
La frase invertida: {texto_corte}
La frase invertida metodo 2: {texto_corte2}""")


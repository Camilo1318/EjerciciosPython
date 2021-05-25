#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

#Modulo o residuo de una division
#El operador módulo no hace otra cosa que devolver el resto de la división entre los dos operandos. En el ejemplo, 7 / 2 sería 3, con 1 de resto, luego el módulo es 1.
# x % y (x y (y) son numeros)

#Cristian Pérez
numero1 = int(input("Introduzca el primero numero: "))
numero2 = int(input("Introduzca el segundo numero: "))
cociente = numero1/numero2
resto = numero1 % numero2

print(f"""
La division entre {numero1} y {numero2} es: 
cociente: {cociente}
residuo: {resto}
""")
print("La division entre",numero1,"y",numero2)



#Juan Diego

primer_numero = int(input("Introduzca un numero: "))
segundo_numero = int(input("Introduzca otro numero: "))
cociente = primer_numero/segundo_numero
resto = primer_numero % segundo_numero

print(f"""La division entre {primer_numero} y {segundo_numero}
cociente: {cociente}
residuo: {resto}
""")
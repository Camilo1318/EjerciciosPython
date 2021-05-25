#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

#Cristian Pérez 
nombre = input("Ingrese su nombre: ")

print(f"""
  Nombre: {nombre.upper()}
  Cantidad de letras: {len(nombre)}
""")

#Juan Diego

nombre = input("Introduzca su nombre: ")

print(f""" 
Nombre : {nombre.upper()}
Numero de letras: {len(nombre)}
""")

#Juan David
nombre = input("¿cual es su nombre?: ")
print((nombre.upper()) + (" Y tiene ") + str(len(nombre)) + (" letras"))
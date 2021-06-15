#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

#Cristian Pérez
numero = int(input("Ingrese un numero: "))
palabras = []
for i in range(numero):
  if numero>0:
    palabras.append(input(f"Ingrese la palabra {i+1}: "))

print("la lista de palabras creada es:",palabras)

antigua_palabra = input("Ingrese la palabra a eliminar: ")

palabras.remove(antigua_palabra)

print("la lista de palabras creada es ahora:",palabras)
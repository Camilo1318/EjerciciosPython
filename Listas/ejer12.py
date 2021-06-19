#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

#Cristian Pérez
numero = int(input("Ingrese un numero: "))
palabras = []
for i in range(numero):
  if numero>0:
    palabras.append(input(f"Ingrese la palabra {i+1}: "))

print("la lista de palabras creada es:",palabras)

antigua_palabra = input("Ingrese la palabra a remplazar: ")

nueva_palabra = input("Ingrese la nueva palabra:")

index = palabras.index(antigua_palabra)
palabras.remove(antigua_palabra)

palabras.insert(index, nueva_palabra)

print("la lista de palabras creada es ahora:",palabras)


#Juan Diego

lista_palabras = []
numero = int(input("Introduzca un numero: "))


for i in range(numero):
    if numero>0:
        minuscula = input(f"Ingrese la palabra {i+1}: ")
        lista_palabras.append(minuscula.lower())


print("La lista de palabras creadas es:", lista_palabras)

antigua_palabra = input("Ingrese la palabra a remplazar: ").lower()
while antigua_palabra not in lista_palabras:
    antigua_palabra = input("Palabra no valida, ingrese una que este en la lista inicial: ")
nueva_palabra = input("Ingrese la nueva palabra: ").lower()



index = lista_palabras.index(antigua_palabra)
lista_palabras.remove(antigua_palabra)

lista_palabras.insert(index, nueva_palabra)

print("La nueva lista de palabras es:", lista_palabras)
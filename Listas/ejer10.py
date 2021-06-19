#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.


#Cristian Pérez
numero = int(input("Ingrese un numero: "))
palabras = []
for i in range(numero):
  if numero>0:
    palabras.append(input(f"Ingrese la palabra {i+1}: "))

palabra = input("Ingrese la palabra a buscar: ")

if palabra in palabras:
  index = palabras.index(palabra)
  print("la poscision de la palabra es:",index)
else:
  print("Palabra no encontrada")

print(palabras)



#Juan Diego

numero = int(input("Introduzca un numero: "))
palabras = []
for i in range(numero):
  if numero>0:
   palabras.append(input(f"Introduzca una palabra {i+1}: "))

palabra = input("Introduzca la palabra a buscar: ")


if palabra in palabras:
  index = palabras.index(palabra)
  print("La posición de la palabra es:", index)
else:
  print("Palabra no encontrada")

print(palabras)

#Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

#Cristian Pérez

numero_palabras = int(input("Ingrese la cantidad de palabras: "))
palabras =[]
for i in range(numero_palabras):
  palabras.append(input(f"Ingrese la palabra {i+1}: "))
print(f"Las palabras agregadas fueron: {palabras}")

new_palabras=[]
for i in range(len(palabras)):
  new_palabras.append(palabras[len(palabras)-i-1])

print(f"La lista alreves es:{new_palabras}")

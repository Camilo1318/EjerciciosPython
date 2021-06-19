#Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

#Cristian Pérez

numero_palabras = int(input("Ingrese la cantidad de palabras: "))
palabras =[]
for i in range(numero_palabras):
  palabras.append(input(f"Ingrese la palabra {i+1}: "))
print(f"Las palabras agregadas fueron: {palabras}")

numero_palabras_eliminar = int(input("Ingrese la cantidad de palabras a eliminar: "))


while(numero_palabras_eliminar>0):
  palabra_a_eliminar = (input(f"Ingrese la palabra a eliminar: "))

  if palabra_a_eliminar in palabras:
    palabras.remove(palabra_a_eliminar)
    print("Removiendo coincidencia...")
    numero_palabras_eliminar -=1
  else:
    print("Palabra no encontrada")

  print("Restan",numero_palabras_eliminar,"por eliminar")
  

print(f"Las palabras finales son: {palabras}")





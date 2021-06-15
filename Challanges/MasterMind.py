#La descripcion del ejercicio se encuentra en la seccion Retos de discord

import random

#Cristian Pérez
print("Cristian Pérez".center(50,"."))
	
#Funciones:
	
def compara_numero(base,new,longitud):
  contador_intentos= 0
  for i in range(len(new)):
    if base[i] == new[i]:
      contador_intentos +=1
  print(f"numeros acertados:{contador_intentos}")
  if contador_intentos == 0:
    print("Intentalo de nuevo...")    
#Main

longitud = int(input("Ingrese la longitud del numero: "))
base = str(random.randint(0, 10**longitud))
new = ""
while (base != new):
  new=input("Intenta adivinar el numero: ")
  if len(new)<=longitud:
    compara_numero(base,new,longitud)
  else:
    print("Numero fuera de rango..")
print("Felicidades!! Adivinaste..")

#Juan Diego   
print("Juan Diego".center(50,"."))


#Funciones:

def compararnumero(base, new, longitud):
  contador_intentos = 0
  for i in range(longitud):
    if base[i] == new[i]:
      contador_intentos +=1 
  print(f"Cantidad de digitos acertados: {contador_intentos}") 

  if contador_intentos == 0:
    print("No has adivinado ningun numero,sigue intentando")
    
#Main

longitud = int(input("Ingrese la longitud a adivinar:"))
base = str(random.randint(0, 10**longitud))
new = ""
while (base != new):
  new = input("Ingrese un numero: ")
  compararnumero(base,new,longitud)
  if len(new)<longitud:
    compararnumero(base, new, longitud)
  else:
      print("Numero fuera de rango")
  

print("¡Felicidades has adivinado el numero!")







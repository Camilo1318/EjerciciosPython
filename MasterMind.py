#La descripcion del ejercicio se encuentra en la seccion Retos de discord

#Cristian Pérez
print("Cristian Pérez".center(50,"."))
base = "2021"

#Funciones:


def compara_numero(base,new):
  contador_intentos= 0
  for i in range(len(new)):
    if base[i] == new[i]:
      contador_intentos +=1
      print(contador_intentos)
      
#Main


flag = True
new = ""
while (base != new or flag):
  flag = False
  new=input("Ingrese un numero: ")
  compara_numero(base,new)



#Juan Diego   
print("Juan Diego".center(50,"."))


base = "5421"

#Funciones:



def compararnumero(base, new):
  contador_intentos = 0
  for i in range(len(new)):
    if base[i] == new[i]:
      contador_intentos +=1 
  print(contador_intentos)
    
#Main


flag = True
new = ""
while (base != new or flag):
  flag = False
  new = input("Ingrese un numero: ")
  compararnumero(base,new)









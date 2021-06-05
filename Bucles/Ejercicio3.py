#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.



#Cristian Pérez

numero = int(input("Ingrse un numero entero: "))

if (numero>0):
  for i in range(1,numero,2):
    print(i,end=",")
else:
  print("Ingrese un numero positivo")

if numero%2 == 0:
  print("\n")
else:
  print(numero,"\n")

#Juan David 
numero = int(input("ingrese un numero entero35 positivo: "))
if (numero>0):
  for i in range(1,numero+1,2):
    print(i, end = ", ")
else:
  print("numero no valido")

print("\n")

#Juan Diego

numero = int(input("Ingrese un numero entero: "))

if (numero<0):
  print("Ingrese un numero valido")
else:
  for i in range(1,numero+1,2):
    print(i,end=",")
    
  
   
#Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

#Cristian Pérez

numero = int(input("Ingrese un numero: "))
tabla_multiplicar = []

for i in range(0,11):
  tabla_multiplicar.append((i+1)*numero)
  # [5 10]
  print(tabla_multiplicar[i],end=",")
  #[5 10]

#Juanda
n = int(input("Ingrese un numero: "))
tablas = []

for i in range(1,11):
  tabla_multiplicar.append(i*n)
  print(tablas)

#Juan Diego
print("Juan Diego".center(50, "*"))


numero = int(input("Introduzca un numero: "))
numero_multiplicado = []

def multiplicacion(numero):
 for i in range(1,11):
    numero_multiplicado.append(i*numero)
    print(numero_multiplicado[i-1],end=",")
    

multiplicacion(numero)
    


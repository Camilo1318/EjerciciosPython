#Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

#Cristian Pérez

numero = int(input("Ingrese un numero: "))
tabla_multiplicar = []

for i in range(1,11):
  tabla_multiplicar.append(i*numero)
  print(tabla_multiplicar[i-1],end=",")


#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#Cristian Pérez


cantidad_a_invertir = int(input("Cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual (%): "))
numero_años = int(input("Ingrese numero de años: "))

for i in range(1,numero_años*12+1):

  print(f"""Capital obtenido al {i} mes: {round(cantidad_a_invertir*(interes_anual/100+1)**i,2)}""")




#Juan Diego

cantidad = int(input("Introduzca la cantidad a invertir: "))
interes_anual = int(input("Interes anual (0 a 100%): "))
numero_años = int(input("Introduzca el numero de años: "))

for i in range(1,numero_años*12): 

 print(f"El capital obtenido en el {i} mes: {round(cantidad*(interes_anual/100+1)**i,2)}")

#Cantidad*(interes_anual+1)**cantidad_años
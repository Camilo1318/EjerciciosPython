#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

#Cristian Pérez

meses = "Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"

numero = int(input("Ingrese un numero de mes: "))

if numero>0 and numero<=len(meses):
  print(f"El mes con ese numero es el: {meses[numero-1]}")
else:
  print("mes no encontado")



#Juan Diego

print("Juan Diego".center(50, "*"))

meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero = int(input("Introduzca un numero del 1 al 12: "))

if numero>=1 and numero<len(meses):
    print(f"El mes correspondiente al numero es: {meses[numero-1]}")
else:
    print("Mes no valido")








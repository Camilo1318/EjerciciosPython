#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

#Para calcular el capital final lo que haremos es multiplicar el capital inicial por uno más los intereses, elevado al número de periodos.

#capital_inicial*(1+intereses)**numero_años

#Cristian Pérez
cantidad = int(input("Ingrese cantidad a invertir: "))
interes_anual = int(input("Ingrese interes (0 a 100 %): "))
numero_años = int(input("Ingrese cantidad de años: "))
capital_obtenido = cantidad*interes_anual/100*numero_años

print(f"Total inversion obtenida: {capital_obtenido}")


#Juan Diego
cantidad = int(input("Introduzca la cantidad a invertir: "))
interes_anual = int(input("Interes anual (0 a 100%): "))
numero_años = int(input("Introduzca el numero de años: "))
capital_anual = cantidad*interes_anual/100*numero_años

print(f"El capital anual obtenido sera: {capital_anual}")

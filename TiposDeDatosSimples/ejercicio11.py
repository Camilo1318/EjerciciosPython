#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

#Cristian Pérez 

interes_anual = 0.04

dinero_anual = int(input("Depositar dinero: "))
total_anual = dinero_anual*interes_anual

print(f"""

Dinero anual: {dinero_anual}
Total Primer año: {round(total_anual*(0.04+1)**1,2)}
Total Segundo año: {round(total_anual*(0.04+1)**2,2)}
Total Tercer año: {round(total_anual*(0.04+1)**3,2)}
""")




#Juan Diego
interes_anual = 0.04

dinero_depositado = int(input("Introduzca la cantidad de dinero depositada en la cuenta de ahorros"))

ahorros1año = dinero_depositado*interes_anual*1
round1año = round(ahorros1año,2)

ahorros2años = dinero_depositado*interes_anual*2 
round2años = round(ahorros2años,2)

ahorros3años = dinero_depositado*interes_anual*3 
round3años = round(ahorros3años,2)

print(f"""
Dinero depositado en la cuenta de ahorros: {dinero_depositado}

Ahorros tras el primer año: {round1año}
Ahorros tras el segundo año: {round2años}
Ahorros tras el tercer año: {round3años}

""")
  

  
#Juan David
dinero = int(input("introduzca la cantidad de dinero que depositara"))
print("sus ahorros al pasar 1 año es " + str(round(dinero*(0.04+1)**1,2)))
print("sus ahorros al pasar 2 año es " + str(round(dinero*(0.04+1)**2,2)))
print("sus ahorros al pasar 3 año es " + str(round(dinero*(0.04+1)**3,2)))



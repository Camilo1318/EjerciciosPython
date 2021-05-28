#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	                       Tipo impositivo
#Menos de 10000€	                    5%
#Entre 10000€ y 20000€	              15%
#Entre 20000€ y 35000€	              20%
#Entre 35000€ y 60000€	              30%
#Más de 60000€	                      45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.



#Yosi
renta = int(input("¿Cúal es su renta anual? --> "))

def Tipo_impositivo(renta):

  if renta < 10000  :
    print("Su tipo impositivo es del 5%")
  elif 10000 <= renta < 20000:
    print("Su tipo impositivo es del 15%")
  elif 20000 <= renta < 35000:
    print("Su tipo impositivo es del 20%")
  elif 35000 <= renta <= 60000:
    print("Su tipo impositivo es del 30%")
  else:
    print("Su tipo impositivo es del 45%")

Tipo_impositivo(renta)



#<>
#Juan Diego
rentan = int(input("Introduzca su renta anual: "))

def impositivo(rentan):

  if rentan<10000:
   print("Le corresponde 5% de tramo impositivo")
  elif rentan>=10000 and rentan<20000:
   print("Le corresponde 15% de tramo impositivo")
  elif rentan>=20000 and rentan<35000:
   print("Le corresponde 20% de tramo impositivo")
  elif rentan>=35000 and rentan<60000:
   print("Le corresponde 30% de tramo impositivo")
  else:
    print("Le corresponde 45% de tramo impositivo")
  

impositivo(rentan)


#Cristian Pérez
renta_anual = int(input("Ingrese la renta anual: "))

if renta_anual<=10000:
  print ("Su imposito es de 5%")
elif renta_anual>10000 and renta_anual<=20000:
  print ("Si imposito es de 15%")
elif renta_anual>20000 and renta_anual<=35000:
  print ("Si imposito es de 20%")
elif renta_anual>35000 and renta_anual<=60000:
  print ("Si imposito es de 30%")
else: 
  print ("Si imposito es de 45%")




#lis

renta = float(input ("ingrese la renta anual: "))

def tipo_impositivo(renta):
  if renta < 10000:
    print ("su impositivo es 5% ")
  elif renta>= 10000 and renta <20000:
    print ("su impositivo es 15% ")
  elif renta>= 20000 and renta <35000:
    print ("su impositivo es 20% ")
  elif renta>= 35000 and renta <60000:
    print ("su impositivo es 30% ")
  else:
   print ("su impositivo es 50% ")

tipo_impositivo(renta)

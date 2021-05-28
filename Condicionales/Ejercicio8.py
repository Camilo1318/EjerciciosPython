#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

    #Nivel	        Puntuación
    #Inaceptable	  0.0
    #Aceptable	    0.4
    #Meritorio	    0.6 o más

#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.



#Yosi
valoracion = float(input("Por favor introduzca su puntuación como empleado: "))

def Calcular_Nivel(valoracion):

  dinero = 2400*valoracion + 2400

  if valoracion == 0.0:
    print(f"Su nivel es Inaceptable con una prima de 2400 ")

  elif valoracion == 0.4:
    print(f"Su nivel es Aceptable con una prima de {dinero} ")

  elif valoracion >= 0.6:
    print(f"Su nivel es Meritorio con una prima de {dinero} ")

Calcular_Nivel(valoracion)



#Juan Diego

evaluacion = float(input("Introduzca la puntuacion del empleado (0.0 , 0.4 o 0.6): "))
beneficio = 2400*evaluacion + 2400

def puntaje(evaluacion):
  if evaluacion == 0.0:
   return f"Este es su beneficio: {beneficio}" 
  elif evaluacion == 0.4:
    return f"Este es su beneficio: {beneficio}" 
  elif evaluacion >= 0.6:
    return f"Este es su beneficio: {beneficio}" 
  else:
    return "Introduzca un valor valido"


print(puntaje(evaluacion))






#Cristian Pérez
puntuacion = float(input("Ingrese su puntuacion: "))
dinero = 2400

if((puntuacion == 0.0 or 0.4 or 0.6) or puntuacion>0.6):
  if puntuacion == 0.0:
    print(f"Su nivel es Inaceptable: {dinero*(puntuacion+1)}")
  elif puntuacion == 0.4:
    print(f"Su nivel es Aceptable: {dinero*(puntuacion+1)}")
  elif puntuacion >= 0.6:
    print(f"Su nivel es Meritorio: {dinero*(puntuacion+1)}")
else:
  print("Puntuacion invalida")



#lis    ¿Si te funciona ya? si muchas gracias

puntuacion = float(input ("ingresar la puntuacion obtenida "))

def valor_dinero(puntuacion):
    print( 2400+(2400*puntuacion))

def rendimiento(puntuacion):
  if puntuacion == 0.0:
    print ("el rendimiento es inaceptable y la cantidad de dinero recibida es de: ", valor_dinero(puntuacion))
  elif puntuacion == 0.4 :
    print ("el rendimiento es aceptable y la cantidad de dinero recibida es de: ", valor_dinero(puntuacion))
  elif puntuacion>= 0.6 :
    print ("el rendimiento es meritorio y la cantidad de dinero recibida es de: ", valor_dinero(puntuacion))
  else:
    print ("el valor no es valido")"
    
rendimiento(puntuacion)
#Debes de imprimir lo que tienes dentro de la función, o si vas a utilizar el return debes imprimirlo donde lo vas a utilizar. 



#Juan David
puntuacion = float(input("¿cual es su puntuacion?:  "))

def nivel(puntuacion):

  prima = 2400*puntuacion+1

  if puntuacion == 0.0:
    print(f"Su nivel es Inaceptable ")

  elif puntuacion == 0.4:
    print(f"Su nivel es Aceptable con una prima de {prima} ")

  elif puntuacion >= 0.6:
    print(f"Su nivel es Meritorio con una prima de {prima} ")

nivel(puntuacion)

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#Pass se utiliza sobre todo para las funciones que no tienen nada en ellas, ejemplo para que despues la puedas modificar, también se puede utilizar si solo quieres que tu código o función llegue hasata cierto punto.

num = int(input("Ingrese un número: "))

def VerificarParImpar(num):
  if num == 0:
    return f"El numero {num} no tiene bando"
  elif num%2 == 0:
    return f"El numero {num} es par"
  else:
    return f"El numero {num} es impar"
    
#9/2 -> 4 -->1

print(VerificarParImpar(num))



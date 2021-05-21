#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Ingrese su primer número que sería su dividendo: "))
num2 = int(input("Ingrese su segundo número que sería su divisor: "))

def calcularDivision(num1,num2):
  if num2 ==  0:
    return f"Lo siento el número {num2} ingresado no puede usarse para ser su divisor"
  else:
    return num1//num2

print(calcularDivision(num1,num2))

#num1/num2 Devuelve un float asi la division resulte ser exacta.
#num1//num2 Devuelve un Entero.
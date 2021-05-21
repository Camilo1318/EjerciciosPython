#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Dígame su edad: "))

def calcularAdultez(edad):
  if edad>= 18:
    return "Eres un Adultero"
  else: 
    return "Eres un niño aún" 

print(calcularAdultez(edad))
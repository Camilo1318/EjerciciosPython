#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#Formula (IMC = peso [kg]/ estatura [m2])

#Juan David
peso= int(input( "ingrese su peso en kg"))
altura= float(input( "ingrese su altura en m"))
altura2= (altura*altura)
imc= (peso/altura2)
print("tu indice de masa corporal es", imc)

#Cristian Pérez
peso = int(input("Ingrese su peso: "))
estatura = int(input("Estatura en centimetros: "))
altura = estatura**2
imc = (peso/altura)*100
print(f"Tu indice de masa corporal es: {imc}")


#Juan Diego
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in mts"))
bmi = (weight/height**2)
MyBmiRound = round(bmi, 2)
print("Your body mass index is", MyBmiRound)


#Yosi
peso = int(input("Ingrese su peso"))
estatura = int(input("Ingrese su estatura"))
altura = estatura**2
masaCorporal = (peso/altura)
print("Su indice de masa corporal ", masaCorporal)


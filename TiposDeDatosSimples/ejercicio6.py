#Escribir un programa que lea un entero positivo,n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: Suma = (n(n+1))/2

#python3 TiposDeDatosSimples/ejercicio6.py

#floor divison 

#Cristian
numero = int(input("Ingrese un numero positivo enter"))
suma = (numero*(numero+1))//2
print(f"La suma de los {numero} primero numeros es: {suma} ")


#Juan David
n= int(input("ingrese un numero positivo"))
suma= (n*(n+1))//2
print("El resultado es:", suma)



#Juan Diego
numero = int(input("Ingrese un numero aleatorio"))
calculo = (numero*(numero+1))//2
print("La suma de los n enteros positivos es: ",calculo)


#Yosi
n = int(input("Ingrese un número"))
formula =  (n*(n+1))/2
print("La respuesta es la siguiente:  ", formula)


